import streamlit as st
import joblib

# Load vectorizer & model
vectorizer = joblib.load("vectorizer.jb")
model = joblib.load("lr_model.jb")

# App title
st.title("📰 Fake News Detector")
st.write("Enter a News Article below to check whether it's **Real** or **Fake**.")

# Text input
news_input = st.text_area("News Article:", '')

# Prediction button
if st.button("Check"):
    if news_input.strip() == "":
        st.warning("⚠️ Please enter some text before checking.")
    else:
        # Transform input & predict
        transformed_input = vectorizer.transform([news_input])
        prediction = model.predict(transformed_input)[0]
        prob = model.predict_proba(transformed_input)[0]

        # Show result
        if prediction == 0:
            st.success(f"✅ This news seems to be **Real**.\n\nConfidence: {prob[0]*100:.2f}%")
        else:
            st.error(f"❌ This news seems to be **Fake**.\n\nConfidence: {prob[1]*100:.2f}%")
