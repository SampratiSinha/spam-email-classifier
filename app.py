import streamlit as st
import pickle
import os

try:
    model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
    vectorizer_path = os.path.join(os.path.dirname(__file__), "vectorizer.pkl")

    model = pickle.load(open(model_path, "rb"))
    vectorizer = pickle.load(open(vectorizer_path, "rb"))

except Exception as e:
    st.error(f"Error loading model: {e}")

st.title("📧 Spam Email Classifier")

st.write("Enter a message to check whether it is Spam or Not Spam")

# Input box
message = st.text_area("Enter Message")

if st.button("Check"):
    if message.strip() != "":
        # Transform input
        data = vectorizer.transform([message])

        # Prediction
        prediction = model.predict(data)[0]
        prob = model.predict_proba(data)[0]

        if prediction == 1:
            st.error(f"Spam Message (Confidence: {round(prob[1]*100,2)}%)")
        else:
            st.success(f"Not Spam (Confidence: {round(prob[0]*100,2)}%)")
    else:
        st.warning("Please enter a message")