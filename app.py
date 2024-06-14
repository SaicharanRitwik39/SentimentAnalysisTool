import numpy as np
np.int = np.int32
np.float = np.float64
np.bool = np.bool_
import streamlit as st
from textblob import TextBlob


# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    sentiment = "Neutral"
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    
    return sentiment, polarity, subjectivity

# Streamlit app
def main():
    st.title("Sentiment Analysis Tool")
    
    # Text input
    text = st.text_area("Enter text for sentiment analysis")
    
    if text:
        sentiment, polarity, subjectivity = analyze_sentiment(text)
        
        st.subheader("Sentiment Analysis Result")
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Polarity:** {polarity}")
        st.write(f"**Subjectivity:** {subjectivity}")

if __name__ == "__main__":
    main()