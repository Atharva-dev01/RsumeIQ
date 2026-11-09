import streamlit as st
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io

def init_session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'current_question' not in st.session_state:
        st.session_state.current_question = None
    if 'current_topic' not in st.session_state:
        st.session_state.current_topic = None
    if 'current_difficulty' not in st.session_state:
        st.session_state.current_difficulty = None
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'current_model' not in st.session_state:
        st.session_state.current_model = 'llama2-70b-4096'

def export_to_pdf(history_data):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    title = Paragraph("Interview Preparation History", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 12))
    
    for item in history_data:
        topic = Paragraph(f"<b>Topic:</b> {item['topic']}", styles['Normal'])
        question = Paragraph(f"<b>Question:</b> {item['question']}", styles['Normal'])
        user_answer = Paragraph(f"<b>Your Answer:</b> {item['user_answer']}", styles['Normal'])
        feedback = Paragraph(f"<b>Feedback:</b> {item['ai_feedback']}", styles['Normal'])
        date = Paragraph(f"<b>Date:</b> {item['timestamp']}", styles['Normal'])
        
        story.extend([topic, question, user_answer, feedback, date])
        story.append(Spacer(1, 12))
    
    doc.build(story)
    buffer.seek(0)
    return buffer

def export_to_csv(history_data):
    df = pd.DataFrame(history_data)
    return df.to_csv(index=False).encode('utf-8')