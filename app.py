from flask import Flask, request, jsonify,render_template
import joblib
import numpy as np
from scipy.sparse import hstack, csr_matrix
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

app = Flask(__name__)
CORS(app)

# Load the necessary saved models
loaded_best_model = joblib.load('models/best_model.joblib')
lda_model = joblib.load('models/lda_model.joblib')
loaded_tfidf_vectorizer = joblib.load('vectors/tfidf_vectorizer.joblib')
count_vectorizer = joblib.load('vectors/count_vectorizer.joblib')
def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    tokens = nltk.word_tokenize(text.lower())
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stopwords.words('english')]
    return ' '.join(tokens)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    reviews = data['reviews']  # List of reviews
    
    # Clean and process each review
    new_reviews_cleaned = [clean_text(review) for review in reviews]

    # Vectorize and predict as before
    new_reviews_vectorized_tfidf = loaded_tfidf_vectorizer.transform(new_reviews_cleaned)
    new_reviews_vectorized_count = count_vectorizer.transform(new_reviews_cleaned)
    topic_features = lda_model.transform(new_reviews_vectorized_count)
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = np.array([sia.polarity_scores(review)['compound'] for review in new_reviews_cleaned]).reshape(-1, 1)

    sentiment_scores_sparse = csr_matrix(sentiment_scores)
    topic_features_sparse = csr_matrix(topic_features)
    new_reviews_features = hstack([new_reviews_vectorized_tfidf, sentiment_scores_sparse, topic_features_sparse])

    new_predictions = loaded_best_model.predict(new_reviews_features)
    quality_mapping = {1: "High Quality", 0: "Low Quality"}
    predicted_qualities = [quality_mapping[pred] for pred in new_predictions]

    results = [{"review": review, "predicted_quality": quality} for review, quality in zip(reviews, predicted_qualities)]
    return jsonify(results)

if __name__ == '__main__':
  app.run(debug=True)
