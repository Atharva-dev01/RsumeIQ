import os
import requests
import json
from dotenv import load_dotenv
import random
import streamlit as st

load_dotenv()

class AIHandler:
    def __init__(self):
        self.groq_api_key = os.getenv('GROQ_API_KEY')
        self.groq_model = os.getenv('GROQ_MODEL', 'llama3-8b-8192')
        
        if not self.groq_api_key:
            st.error("❌ GROQ_API_KEY not found in environment variables. Please check your .env file.")
            # Don't raise error, just use fallback mode
            self.groq_api_key = None

    def get_available_models(self):
        """Get list of available Groq models"""
        return [
            "llama-3.1-8b-instant",
            "llama3-8b-8192",
            "llama3-70b-8192", 
            "mixtral-8x7b-32768",
            "gemma-7b-it"
        ]

    def set_model(self, model_name):
        """Change the Groq model"""
        available_models = self.get_available_models()
        if model_name in available_models:
            self.groq_model = model_name
            return True
        return False

    def generate_question(self, topic, difficulty):
        """Generate interview question"""
        if not self.groq_api_key:
            return self._fallback_question(topic, difficulty)
            
        prompt = f"""
        Generate one {difficulty.lower()} level interview question about {topic}.
        Return ONLY the question without any additional text or explanations.
        The question should be challenging and relevant to real-world interviews.
        
        Example format for "Python programming" topic:
        "Can you explain the difference between lists and tuples in Python, and when you would use each?"
        
        Important: Return ONLY the question text, no prefixes like "Question:" or numbering.
        """
        
        try:
            return self._groq_generate(prompt, max_tokens=150)
        except Exception as e:
            st.warning(f"⚠️ Using fallback questions: {e}")
            return self._fallback_question(topic, difficulty)

    def evaluate_answer(self, question, user_answer, difficulty):
        """Evaluate user's answer"""
        if not self.groq_api_key:
            return self._fallback_feedback()
            
        prompt = f"""
        You are an experienced technical interviewer. Please evaluate this interview response.

        QUESTION: {question}
        USER'S ANSWER: {user_answer}
        DIFFICULTY LEVEL: {difficulty}

        Please provide:
        1. Constructive feedback on the user's answer (what was good, what could be improved)
        2. A sample ideal answer that would be expected in a real interview

        Format your response EXACTLY as follows:
        FEEDBACK: [your detailed feedback here]
        IDEAL_ANSWER: [comprehensive ideal answer here]

        Guidelines:
        - Be constructive and helpful, not critical
        - Highlight strengths and suggest improvements
        - For {difficulty} level, adjust expectations accordingly
        - Ideal answer should demonstrate depth and clarity
        """
        
        try:
            response = self._groq_generate(prompt, max_tokens=800)
            return self._parse_feedback(response)
        except Exception as e:
            st.warning(f"⚠️ Using fallback feedback: {e}")
            return self._fallback_feedback()

    def _groq_generate(self, prompt, max_tokens=1024, temperature=0.7):
        """Generate response using Groq API"""
        if not self.groq_api_key:
            raise Exception("Groq API key not configured")

        # Updated Groq API endpoint
        url = "https://api.groq.com/openai/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {self.groq_api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "model": self.groq_model,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "top_p": 1,
            "stream": False
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            
            # Debug information
            print(f"API URL: {url}")
            print(f"Model: {self.groq_model}")
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 404:
                raise Exception("Groq API endpoint not found. The API may have been updated.")
            elif response.status_code == 401:
                raise Exception("Invalid API key. Please check your GROQ_API_KEY in .env file")
            elif response.status_code == 429:
                raise Exception("Rate limit exceeded. Please try again later.")
            elif response.status_code != 200:
                raise Exception(f"API returned status {response.status_code}: {response.text}")
                
            data = response.json()
            
            if 'choices' not in data or len(data['choices']) == 0:
                raise Exception("No response generated from API")
                
            return data['choices'][0]['message']['content'].strip()
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error: {str(e)}")
        except Exception as e:
            raise Exception(f"Groq API error: {str(e)}")

    def _parse_feedback(self, response):
        """Parse the feedback response"""
        lines = response.split('\n')
        feedback = ""
        ideal_answer = ""
        
        for line in lines:
            line = line.strip()
            if line.startswith('FEEDBACK:'):
                feedback = line.split(':', 1)[1].strip()
            elif line.startswith('IDEAL_ANSWER:'):
                ideal_answer = line.split(':', 1)[1].strip()
        
        # If parsing fails, use the entire response as feedback
        if not feedback:
            feedback = response
        if not ideal_answer:
            ideal_answer = "Review the feedback above to improve your answer."
        
        return {
            "feedback": feedback,
            "ideal_answer": ideal_answer
        }

    def _fallback_question(self, topic, difficulty):
        """Fallback question generation"""
        questions = {
            "easy": [
                f"What are the basic concepts of {topic}?",
                f"Explain {topic} in simple terms.",
                f"Why is {topic} important in today's world?",
                f"Can you define what {topic} means?",
                f"What are the main components of {topic}?"
            ],
            "medium": [
                f"Describe a real-world application of {topic}.",
                f"What are the main challenges in working with {topic}?",
                f"How would you approach learning {topic} effectively?",
                f"Compare and contrast {topic} with related technologies.",
                f"What are the best practices for working with {topic}?"
            ],
            "hard": [
                f"Discuss the future trends and advancements in {topic}.",
                f"What are the ethical considerations in {topic}?",
                f"How would you design a complex system using {topic} principles?",
                f"What are the scalability limitations of {topic} and how would you address them?",
                f"Explain the most complex concept in {topic} to a non-technical audience."
            ]
        }
        return random.choice(questions.get(difficulty.lower(), questions["medium"]))

    def _fallback_feedback(self):
        """Fallback feedback"""
        return {
            "feedback": "This is a good start! Try to provide more specific examples and structure your answer better. Consider explaining the 'why' behind your answer and include relevant technical details.",
            "ideal_answer": "A comprehensive answer would include: 1) Clear explanation of concepts, 2) Specific examples or use cases, 3) Technical details relevant to the topic, 4) Best practices or industry standards, and 5) Practical implications or real-world applications."
        }