import ast
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load song data from CSV file
song_data = pd.read_csv("../data/data.csv")

# Convert the string representation of a list to an actual list
song_data['artists'] = song_data['artists'].apply(ast.literal_eval)

# Convert 'release_date' to datetime format
song_data['release_date'] = pd.to_datetime(song_data['release_date'], format='%Y', errors='coerce')

# Extract year from the datetime
song_data['release_year'] = song_data['release_date'].dt.year




# Extract relevant features for scaling and clustering
selected_features = ['valence', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness']
X = song_data[selected_features]

# Data preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert the scaled data to a DataFrame
X_scaled_df = pd.DataFrame(X_scaled, columns=[f"{feat}_scaled" for feat in selected_features])

# Add scaled features to the original DataFrame
song_data = pd.concat([song_data, X_scaled_df], axis=1)

# Save preprocessed data (including scaled features) to a new CSV file
preprocessed_file_path = "../data/processed_song_data.csv"
song_data.to_csv(preprocessed_file_path, index=False)