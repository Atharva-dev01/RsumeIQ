import sqlite3
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

class Database:
    def __init__(self):
        self.db_path = os.getenv('DB_PATH', 'interview_prep.db')
        self.init_db()

    def _get_connection(self):
        """Get a new database connection"""
        try:
            connection = sqlite3.connect(self.db_path, check_same_thread=False)
            connection.row_factory = sqlite3.Row  # enables dict-like access
            return connection
        except sqlite3.Error as err:
            print(f"❌ Database connection error: {err}")
            return None

    def init_db(self):
        """Initialize database tables"""
        connection = self._get_connection()
        if not connection:
            return False
            
        try:
            cursor = connection.cursor()
            
            # Create users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create history table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    topic TEXT NOT NULL,
                    difficulty TEXT NOT NULL,
                    question TEXT NOT NULL,
                    user_answer TEXT NOT NULL,
                    ai_feedback TEXT NOT NULL,
                    ideal_answer TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (username) REFERENCES users(username) ON DELETE CASCADE
                )
            """)
            
            connection.commit()
            print("✅ Database tables initialized successfully")
            return True
        except sqlite3.Error as err:
            print(f"❌ Error initializing tables: {err}")
            return False
        finally:
            connection.close()

    def execute_query(self, query, params=None):
        """Execute database query"""
        connection = self._get_connection()
        if not connection:
            return None
            
        try:
            # Convert MySQL-style %s placeholders to SQLite ? placeholders
            query = query.replace('%s', '?')
            
            cursor = connection.cursor()
            cursor.execute(query, params or ())
            
            if query.strip().lower().startswith('select'):
                rows = cursor.fetchall()
                # Convert sqlite3.Row objects to dicts
                result = [dict(row) for row in rows]
            else:
                connection.commit()
                result = cursor.lastrowid
            
            cursor.close()
            return result
        except sqlite3.Error as err:
            print(f"❌ Database query error: {err}")
            print(f"   Query: {query}")
            return None
        finally:
            connection.close()