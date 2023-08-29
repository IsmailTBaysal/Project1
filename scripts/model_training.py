import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

from scripts.recommendation_engine import trained_model

# Load preprocessed song data
preprocessed_data = pd.read_csv("data/preprocessed_song_data.csv")

# Split data into training and testing sets
train_data, test_data = train_test_split(preprocessed_data, test_size=0.2, random_state=42)

# Example: Train a content-based recommendation model using TF-IDF and cosine similarity

# Save the trained model using joblib
joblib.dump(trained_model, "models/content_based_model.pkl")
