import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

df = pd.read_csv("/Users/prason/Downloads/spam.csv", encoding="latin-1")
df = df[['v1', 'v2']]
df.columns = ['label', 'message']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])

model.fit(X_train, y_train)
joblib.dump(model, 'model.pkl')

import streamlit as st
import joblib

try:
    model = joblib.load('model.pkl')
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.title("Spam or Ham Email Classifier")
st.write("Enter an email message below, and the model will classify it as spam or ham.")

user_input = st.text_area("Your Message:")

if st.button("Classify"):
    if not user_input or user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        try:
            safe_input = str(user_input).strip()
            prediction = model.predict([safe_input])[0]
            result = "Spam" if prediction == 1 else "Ham"
            st.success(f"The message is classified as: {result}")
        except Exception as e:
            st.error(f"An error occurred during prediction: {str(e)}")