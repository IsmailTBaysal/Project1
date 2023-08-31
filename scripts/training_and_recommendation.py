import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.preprocessing import StandardScaler
from app.models import Song

# Load song data from CSV file
song_data = pd.read_csv("../data/processed_song_data.csv")

# Extract relevant features
selected_features = ['valence_scaled', 'acousticness_scaled', 'danceability_scaled', 'energy_scaled',
                     'instrumentalness_scaled', 'liveness_scaled', 'speechiness_scaled']
X = song_data[selected_features]


'''
Create a song instance
Set new features (from API)

song_features = song.get_features() 

'''


# Normalize user input based on the scaler used during preprocessing
scaler = StandardScaler()
user_input_scaled = scaler.fit_transform([song_features])

# Find the closest cluster for user input
kmeans = KMeans(n_clusters=20, n_init=10, random_state=42)
clusters = kmeans.fit_predict(X)
closest_cluster = kmeans.predict(user_input_scaled)

# Get the songs in the closest cluster
songs_in_cluster = song_data[song_data['cluster'] == closest_cluster[0]]

# Calculate distances between user input and songs in the cluster
song_distances = euclidean_distances(user_input_scaled, songs_in_cluster[selected_features])

# Get the indices of the 10 closest songs
closest_song_indices = np.argsort(song_distances.flatten())[:10]

# Get the details of the recommended songs
recommended_songs = songs_in_cluster.iloc[closest_song_indices]

'''
Create recommended song instances

Set new features from recommended_songs

get it from somewhere else to show the user

'''
