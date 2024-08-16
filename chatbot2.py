import streamlit as st
import google.generativeai as genai
import time

API_KEY = ""

# Set up the page configuration
st.set_page_config(
    page_title="Gemini Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for styling
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

body {
    font-family: 'Roboto', sans-serif;
    background-color: #f0f4f8;
    color: #333;
}

header {
    background-color: #4A90E2;
    padding: 10px;
    border-radius: 10px;
}

h1 {
    color: #ffffff;
    text-align: center;
    font-size: 2.5rem;
    font-weight: 700;
}

footer {
    font-size: 0.9rem;
    color: #888;
    text-align: center;
    margin-top: 20px;
}

.chat-container {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
}

.chat-input {
    width: 100%;
    padding: 15px;
    border-radius: 8px;
    border: 1px solid #ddd;
    font-size: 1rem;
    margin-bottom: 20px;
}

.chat-response {
    font-size: 1rem;
    line-height: 1.5;
    color: #555;
}

.chat-title {
    font-size: 1.75rem;
    color: #4A90E2;
    font-weight: 500;
    margin-bottom: 10px;
}

.button {
    background-color: #4A90E2;
    color: #ffffff;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    cursor: pointer;
    font-size: 1rem;
    font-weight: 500;
}

.button:hover {
    background-color: #357ABD;
}
</style>
"""

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Page title
st.markdown('<header><h1>Gemini-Powered Chatbot</h1></header>', unsafe_allow_html=True)

# Load the model
with st.spinner('Loading Gemini model...'):
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
    except Exception as e:
        st.error(f"Error configuring API or creating model: {e}")

# Function to get response from the model
def get_response_from_model(user_input):
    try:
        with st.spinner('Generating response...'):
            response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return None

# User input
user_input = st.text_input("Enter your prompt:", placeholder="Type your message here...", help="Press Enter to send")

# Handle user input and response
if user_input:
    response = get_response_from_model(user_input)
    if response:
        # Display user input and response directly without session
        st.markdown(f'<div class="chat-container"><p class="chat-response"><strong>User:</strong> {user_input}</p><p class="chat-response"><strong>Bot:</strong> {response}</p></div>', unsafe_allow_html=True)

# Footer
st.markdown('<footer>Powered by Gemini AI | Developed with Streamlit</footer>', unsafe_allow_html=True)
