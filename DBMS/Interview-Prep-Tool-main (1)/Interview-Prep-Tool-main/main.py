import streamlit as st
import pandas as pd
import plotly.express as px
from database import Database
from auth import Auth
from ai_handler import AIHandler
from utils import init_session_state, export_to_pdf, export_to_csv
import time
from streamlit_option_menu import option_menu


# Page configuration
st.set_page_config(
    page_title="AI Interview Prep",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
init_session_state()

# Add this line to fix the current_model issue
if 'current_model' not in st.session_state:
    st.session_state.current_model = 'llama3-8b-8192'

# Navigation state
if 'nav_page' not in st.session_state:
    st.session_state.nav_page = 'Dashboard'

# Store classes in session state to prevent re-initialization - ONLY ONCE
if 'app_initialized' not in st.session_state:
    try:
        st.session_state.db = Database()
        st.session_state.auth = Auth()
        st.session_state.ai = AIHandler()
        st.session_state.db_connected = True
        st.session_state.app_initialized = True
        print("✅ Application initialized successfully")
    except Exception as e:
        st.session_state.db_connected = False
        st.session_state.app_initialized = True
        st.error(f"❌ Initialization error: {e}")
        st.stop()

# Use the classes from session state
db = st.session_state.get('db')
auth = st.session_state.get('auth')
ai = st.session_state.get('ai')

if not db or not auth or not ai:
    st.error("❌ Application failed to initialize. Please refresh the page.")
    st.stop()

# Custom CSS for better styling
st.markdown("""hon 
<style>
    /* Headers */
    .main-header {
        font-size: 2.2rem;
        text-align: center;
            o ./
        margin-bottom: 2rem;
        font-weight: 600;
        letter-spacing: -0.025em;
        padding: 1rem 0;
        color: var(--text-color);
    }
    
    /* Question box - Subtle shadow */
    .question-box {
        background-color: var(--secondary-background-color);
        border-radius: 8px;
        padding: 24px;
        margin: 20px 0;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    }
    
    .question-box h3 {
        font-weight: 500;
        margin-bottom: 12px;
        font-size: 1.1rem;
    }
    
    .question-box p {
        font-size: 15px;
        line-height: 1.6;
    }
    
    /* Feedback boxes */
    .info-box {
        background-color: var(--secondary-background-color);
        border-left: 4px solid var(--primary-color);
        border-radius: 4px;
        padding: 16px 20px;
        margin: 15px 0;
    }
    
    .success-box {
        background-color: var(--secondary-background-color);
        border-left: 4px solid #22c55e;
        border-radius: 4px;
        padding: 16px 20px;
        margin: 15px 0;
    }
    
    /* Form containers */
    .stForm {
        border-radius: 8px;
        padding: 24px;
        margin: 20px 0;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    }
</style>
""", unsafe_allow_html=True)

def login_page():
    # Main header with good contrast
    st.markdown(
        '<div class="main-header">AI Interview Preparation System</div>', 
        unsafe_allow_html=True
    )
    
    # Center the login form
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
            <h3>Welcome to Your Interview Coach</h3>
            <p>Practice with AI-powered questions and get instant feedback</p>
        </div>
        """, unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["Login", "Sign Up"])
        
        with tab1:
            with st.form("login_form", clear_on_submit=False):
                st.subheader("Login to Your Account")
                
                username = st.text_input(
                    "Username",
                    placeholder="Enter your username"
                )
                password = st.text_input(
                    "Password", 
                    type="password",
                    placeholder="Enter your password"
                )
                
                login_btn = st.form_submit_button(
                    "Login to Dashboard", 
                    use_container_width=True
                )
                
                if login_btn:
                    if username and password:
                        user = auth.login_user(username, password)
                        if user:
                            st.session_state.logged_in = True
                            st.session_state.username = username
                            st.success("Login successful! Redirecting...")
                            time.sleep(1)
                            st.rerun()
                        else:
                            st.error("Invalid username or password")
                    else:
                        st.warning("Please fill in all fields")
        
        with tab2:
            with st.form("signup_form", clear_on_submit=False):
                st.subheader("Create New Account")
                
                new_username = st.text_input(
                    "Choose Username",
                    placeholder="Enter a username"
                )
                email = st.text_input(
                    "Email",
                    placeholder="Enter your email"
                )
                new_password = st.text_input(
                    "Choose Password", 
                    type="password",
                    placeholder="Create a password"
                )
                confirm_password = st.text_input(
                    "Confirm Password", 
                    type="password",
                    placeholder="Confirm your password"
                )
                
                signup_btn = st.form_submit_button(
                    "Create Account", 
                    use_container_width=True
                )
                
                if signup_btn:
                    if new_username and email and new_password and confirm_password:
                        if new_password == confirm_password:
                            if auth.register_user(new_username, email, new_password):
                                st.success("Account created successfully! Please login.")
                            else:
                                st.error("Username or email already exists")
                        else:
                            st.error("Passwords do not match")
                    else:
                        st.warning("Please fill in all fields")

def dashboard():
    st.sidebar.title(f"Welcome, {st.session_state.username}!")
    
    menu = ["Dashboard", "Practice Interview", "History", "Profile", "Logout"]
    icons = ["house", "chat-text", "clock-history", "person", "box-arrow-right"]
    default_idx = menu.index(st.session_state.nav_page) if st.session_state.nav_page in menu else 0
    
    with st.sidebar:
        choice = option_menu(
            "Navigation", 
            menu, 
            icons=icons, 
            menu_icon="cast", 
            default_index=default_idx,
            styles={
                "container": {"padding": "0!important", "background-color": "transparent"},
                "icon": {"color": "#cbd5e1", "font-size": "18px"}, 
                "nav-link": {"color": "#f8fafc", "font-size": "15px", "text-align": "left", "margin":"4px 0", "--hover-color": "#1e293b", "border-radius": "6px"},
                "nav-link-selected": {"background-color": "#3b82f6", "color": "white", "font-weight": "500"},
            },
            key="main_nav_menu"
        )
        
    st.session_state.nav_page = choice
    
    if choice == "Dashboard":
        show_dashboard()
    elif choice == "Practice Interview":
        practice_interview()
    elif choice == "History":
        show_history()
    elif choice == "Profile":
        show_profile()
    elif choice == "Logout":
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.current_question = None
        st.session_state.chat_history = []
        st.session_state.nav_page = 'Dashboard'
        st.rerun()

def show_dashboard():
    st.markdown('<div class="main-header">Dashboard</div>', unsafe_allow_html=True)
    
    # User stats
    col1, col2, col3 = st.columns(3)
    
    # Get user stats from database
    history_query = "SELECT COUNT(*) as total FROM history WHERE username = %s"
    history_result = db.execute_query(history_query, (st.session_state.username,))
    total_sessions = history_result[0]['total'] if history_result else 0
    
    topics_query = "SELECT COUNT(DISTINCT topic) as topics FROM history WHERE username = %s"
    topics_result = db.execute_query(topics_query, (st.session_state.username,))
    total_topics = topics_result[0]['topics'] if topics_result else 0
    
    recent_query = "SELECT timestamp FROM history WHERE username = %s ORDER BY timestamp DESC LIMIT 1"
    recent_result = db.execute_query(recent_query, (st.session_state.username,))
    last_session = recent_result[0]['timestamp'] if recent_result else "No sessions yet"
    
    with col1:
        st.metric("Total Practice Sessions", total_sessions)
    with col2:
        st.metric("Topics Covered", total_topics)
    with col3:
        st.metric("Last Session", str(last_session)[:10] if last_session != "No sessions yet" else "No sessions yet")
    
    # Practice Visualization
    st.markdown("---")
    st.subheader("Your Practice Analytics")
    
    topic_dist_query = "SELECT topic, COUNT(*) as count FROM history WHERE username = %s GROUP BY topic"
    topic_dist = db.execute_query(topic_dist_query, (st.session_state.username,))
    
    if topic_dist:
        df_topics = pd.DataFrame(topic_dist)
        fig = px.pie(df_topics, values='count', names='topic', hole=0.4, 
                     color_discrete_sequence=px.colors.qualitative.Pastel)
        fig.update_layout(margin=dict(t=20, b=20, l=20, r=20), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Complete an interview session to see your personalized analytics here!")
        
    st.markdown("---")
    
    # Quick actions
    st.subheader("Quick Actions")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Start New Practice", use_container_width=True, key="dashboard_practice"):
            st.session_state.current_question = None
            st.session_state.chat_history = []
            st.session_state.nav_page = 'Practice Interview'
            st.rerun()
    
    with col2:
        if st.button("View History", use_container_width=True, key="dashboard_history"):
            st.session_state.nav_page = 'History'
            st.rerun()
    
    with col3:
        if st.button("Update Profile", use_container_width=True, key="dashboard_profile"):
            st.session_state.nav_page = 'Profile'
            st.rerun()

def practice_interview():
    st.markdown('<div class="main-header">AI Interview Practice</div>', unsafe_allow_html=True)
    
    # Model selection in sidebar
    with st.sidebar.expander("AI Settings"):
        available_models = ai.get_available_models()
        selected_model = st.selectbox("AI Model", available_models, index=0, key="model_select")
        
        if st.session_state.current_model != selected_model:
            ai.set_model(selected_model)
            st.session_state.current_model = selected_model

    # If no session is active, show pre-interview setup
    if not st.session_state.current_question:
        st.markdown("### Pre-Interview Setup")
        st.markdown("Configure your mock interview session below.")
        
        topics = [
            "Data Science", "Machine Learning", "Software Engineering",
            "Web Development", "Data Structures", "Algorithms",
            "Python Programming", "Java Development", "Frontend Development",
            "Backend Development", "DevOps", "Cloud Computing",
            "System Design", "Database Management", "Mobile Development"
        ]
        
        col1, col2 = st.columns(2)
        with col1:
            selected_topic = st.selectbox("Select Topic", topics, key="topic_select")
        with col2:
            difficulty = st.radio("Difficulty Level", ["Easy", "Medium", "Hard"], horizontal=True, key="difficulty_select")
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("Start Interview", use_container_width=True, key="start_interview_btn"):
            with st.spinner(f"Generating {difficulty.lower()} question..."):
                question = ai.generate_question(selected_topic, difficulty)
                if question:
                    st.session_state.current_question = question
                    st.session_state.current_topic = selected_topic
                    st.session_state.current_difficulty = difficulty
                    st.session_state.chat_history = [{"role": "assistant", "content": question}]
                    st.rerun()
                else:
                    st.error("Failed to generate question. Please try again.")
    else:
        # Active session conversational UI
        col1, col2 = st.columns([3, 1])
        with col1:
            st.info(f"**Topic:** {st.session_state.current_topic} | **Difficulty:** {st.session_state.current_difficulty}")
        with col2:
            if st.button("End Session", key="end_session_btn", use_container_width=True):
                st.session_state.current_question = None
                st.session_state.chat_history = []
                st.rerun()
                
        st.markdown("---")
        
        # Display chat history
        for msg in st.session_state.chat_history:
            with st.chat_message(msg['role']):
                st.markdown(msg['content'])
        
        # User answer input
        user_answer = st.chat_input("Type your answer here...")
        if user_answer:
            # Append user message instantly
            st.session_state.chat_history.append({"role": "user", "content": user_answer})
            
            with st.chat_message("user"):
                st.markdown(user_answer)
                
            with st.chat_message("assistant"):
                with st.spinner("Analyzing..."):
                    feedback = ai.evaluate_answer(
                        st.session_state.current_question, 
                        user_answer, 
                        st.session_state.current_difficulty
                    )
                    
                    # Store in database
                    query = """
                    INSERT INTO history (username, topic, difficulty, question, user_answer, ai_feedback, ideal_answer)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
                    db.execute_query(query, (
                        st.session_state.username,
                        st.session_state.current_topic,
                        st.session_state.current_difficulty,
                        st.session_state.current_question,
                        user_answer,
                        feedback['feedback'],
                        feedback['ideal_answer']
                    ))
                    
                    ai_response = f"**Feedback:**\n{feedback['feedback']}\n\n**Ideal Answer:**\n{feedback['ideal_answer']}"
                    st.markdown(ai_response)
                    st.session_state.chat_history.append({"role": "assistant", "content": ai_response})

def show_history():
    st.markdown('<div class="main-header">Practice History</div>', unsafe_allow_html=True)
    
    # Fetch user history
    query = """
    SELECT topic, difficulty, question, user_answer, ai_feedback, ideal_answer, timestamp
    FROM history WHERE username = %s ORDER BY timestamp DESC
    """
    history = db.execute_query(query, (st.session_state.username,))
    
    if not history:
        st.info("No practice sessions found. Start practicing to see your history here!")
        return
    
    # Export options
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Export as PDF", key="export_pdf"):
            pdf_buffer = export_to_pdf(history)
            st.download_button(
                label="Download PDF",
                data=pdf_buffer,
                file_name="interview_history.pdf",
                mime="application/pdf"
            )
    
    with col2:
        csv_data = export_to_csv(history)
        st.download_button(
            label="Export as CSV",
            data=csv_data,
            file_name="interview_history.csv",
            mime="text/csv"
        )
    
    # Display history
    if history:
        # Create a summary dataframe
        df = pd.DataFrame(history)
        display_df = df[['timestamp', 'topic', 'difficulty', 'question']].copy()
        
        st.markdown("### Session Overview")
        st.dataframe(
            display_df, 
            use_container_width=True, 
            hide_index=True,
            column_config={
                "timestamp": st.column_config.DatetimeColumn("Date & Time", format="DD MMM YYYY, h:mm a"),
                "topic": "Topic",
                "difficulty": "Difficulty",
                "question": "Question Snippet"
            }
        )
        
        st.markdown("### Session Details")
        st.markdown("Select a past session below to review your answers and feedback.")
        
        session_options = [f"{s['timestamp']} - {s['topic']} ({s['difficulty']})" for s in history]
        selected_session_idx = st.selectbox("Select Session to Review", range(len(session_options)), format_func=lambda x: session_options[x], label_visibility="collapsed")
        
        if selected_session_idx is not None:
            session = history[selected_session_idx]
            st.markdown(f'<div class="question-box"><strong>Question:</strong><br><span>{session["question"]}</span></div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f'<div class="success-box"><strong>Your Answer:</strong><br><span>{session["user_answer"]}</span></div>', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<div class="info-box"><strong>AI Feedback:</strong><br><span>{session["ai_feedback"]}</span></div>', unsafe_allow_html=True)
                
            st.markdown(f'<div style="background-color:var(--secondary-background-color); padding: 20px; border-radius: 8px; border: 1px solid var(--secondary-background-color);"><strong>Ideal Answer:</strong><br><span>{session["ideal_answer"]}</span></div>', unsafe_allow_html=True)

def show_profile():
    st.markdown('<div class="main-header">User Profile</div>', unsafe_allow_html=True)
    
    # Get current user info
    query = "SELECT username, email FROM users WHERE username = %s"
    user_info = db.execute_query(query, (st.session_state.username,))
    
    if not user_info:
        st.error("User not found")
        return
        
    user_info = user_info[0]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Profile Information")
        st.info(f"**Username:** {user_info['username']}")
        st.info(f"**Email:** {user_info['email']}")
        
        # Update profile form
        with st.form("update_profile"):
            st.subheader("Update Profile")
            new_username = st.text_input("New Username", value=user_info['username'], key="new_username")
            new_email = st.text_input("New Email", value=user_info['email'], key="new_email")
            update_btn = st.form_submit_button("Update Profile")
            
            if update_btn:
                if auth.update_user(st.session_state.username, new_username, new_email):
                    st.session_state.username = new_username
                    st.success("Profile updated successfully!")
                    st.rerun()
                else:
                    st.error("Error updating profile")
    
    with col2:
        st.subheader("Statistics")
        
        # Get user stats
        stats_query = """
        SELECT 
            COUNT(*) as total_sessions,
            COUNT(DISTINCT topic) as topics_covered,
            MAX(timestamp) as last_active
        FROM history WHERE username = %s
        """
        stats = db.execute_query(stats_query, (st.session_state.username,))
        
        if stats:
            stats = stats[0]
            st.metric("Total Practice Sessions", stats['total_sessions'])
            st.metric("Topics Covered", stats['topics_covered'])
            st.metric("Last Active", str(stats['last_active'])[:10] if stats['last_active'] else "Never")
        else:
            st.metric("Total Practice Sessions", 0)
            st.metric("Topics Covered", 0)
            st.metric("Last Active", "Never")
        
        # Danger zone
        st.subheader("Danger Zone")
        with st.form("delete_account"):
            st.warning("This action cannot be undone. All your data will be permanently deleted.")
            confirm_text = st.text_input("Type 'DELETE' to confirm", key="delete_confirm")
            delete_btn = st.form_submit_button("Delete Account", type="secondary")
            
            if delete_btn and confirm_text == "DELETE":
                if auth.delete_user(st.session_state.username):
                    st.session_state.logged_in = False
                    st.session_state.username = None
                    st.success("Account deleted successfully!")
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("Error deleting account")

def main():
    if not st.session_state.logged_in:
        login_page()
    else:
        dashboard()

if __name__ == "__main__":
    main()