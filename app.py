import streamlit as st
import joblib
model = joblib.load("news-classification-model.pkl")
news_labels = {'0':'Tech', '1':'Business','2':'Sports', '3':'Entertainment', '4':'Politics'}
st.title("News Classification")
user_input = st.text_area("Enter your text here:")

if st.button("Predict"):
    #print(user_input)
    predicted_sentiment = model.predict([user_input])[0]
    print("Predicted Label:" + str(predicted_sentiment))
    predicted_news_label = news_labels[str(predicted_sentiment)]
    # Display predicted sentiment
    st.info(f"Predicted News Category: {predicted_news_label}")
    

