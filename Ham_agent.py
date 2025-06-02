import streamlit as st
import os
import json
from dotenv import load_dotenv
from groq import Groq

st.title("Spam and Ham Email Classification Agent")
st.write("Advanced AI agent for email classification using Groq models")

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")
client = Groq(api_key=GROQ_API_KEY)

available_models = [
    "llama3-70b-8192", 
    "llama3-8b-8192",
    "mixtral-8x7b-32768", 
    "gemma2-9b-it"
]

model_choice = st.selectbox("Choose AI Model", available_models)

email_content = st.text_area("Enter email content for analysis:", height=200)

if st.button("Analyze Email"):
    if email_content.strip():
        system_prompt = """You are an expert email security agent specializing in spam detection. 
Analyze email content with precision and provide classification with detailed reasoning.

Classification criteria:
- SPAM: Promotional content, phishing attempts, suspicious links, urgent money requests, 
  lottery/prize notifications, fake offers, malicious attachments mentions
- HAM: Personal communication, business correspondence, legitimate notifications, 
  professional emails, authentic service updates

Always respond in valid JSON format only."""

        user_prompt = f"""Classify this email and explain your decision:

Email Content: {email_content}

Required JSON response format:
{{
    "email_type": "spam" or "ham",
    "reason": "detailed explanation for classification"
}}"""

        try:
            completion = client.chat.completions.create(
                model=model_choice,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=400,
                temperature=0.1
            )
            
            result = completion.choices[0].message.content.strip()
            
            try:
                parsed_result = json.loads(result)
                
                if parsed_result["email_type"] == "spam":
                    st.error(f"Classification: {parsed_result['email_type'].upper()}")
                else:
                    st.success(f"Classification: {parsed_result['email_type'].upper()}")
                
                st.info(f"Analysis: {parsed_result['reason']}")
                
                with st.expander("Raw JSON Response"):
                    st.code(json.dumps(parsed_result, indent=2))
                    
            except json.JSONDecodeError:
                st.warning("Response format issue. Raw response:")
                st.text(result)
                
        except Exception as error:
            st.error(f"Classification failed: {str(error)}")
    else:
        st.warning("Please provide email content to analyze.")
