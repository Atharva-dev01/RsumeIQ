import bcrypt
from database import Database

class Auth:
    def __init__(self):
        self.db = Database()

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def verify_password(self, password, hashed):
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

    def register_user(self, username, email, password):
        hashed_password = self.hash_password(password)
        
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        result = self.db.execute_query(query, (username, email, hashed_password))
        return result is not None

    def login_user(self, username, password):
        query = "SELECT * FROM users WHERE username = %s"
        user = self.db.execute_query(query, (username,))
        
        if user and len(user) > 0:
            if self.verify_password(password, user[0]['password']):
                return user[0]
        return None

    def update_user(self, username, new_username=None, new_email=None):
        if new_username and new_email:
            query = "UPDATE users SET username = %s, email = %s WHERE username = %s"
            return self.db.execute_query(query, (new_username, new_email, username))
        elif new_username:
            query = "UPDATE users SET username = %s WHERE username = %s"
            return self.db.execute_query(query, (new_username, username))
        elif new_email:
            query = "UPDATE users SET email = %s WHERE username = %s"
            return self.db.execute_query(query, (new_email, username))
        return None

    def delete_user(self, username):
        # First delete user's history
        self.db.execute_query("DELETE FROM history WHERE username = %s", (username,))
        # Then delete user
        return self.db.execute_query("DELETE FROM users WHERE username = %s", (username,))