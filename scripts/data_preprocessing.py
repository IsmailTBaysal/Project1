import pandas as pd

from scripts.model_training import preprocessed_data

# Load song data from CSV file
song_data = pd.read_csv("data/spotify_data.csv")

# Data preprocessing steps
# Remove duplicates,
# handle missing values,
# normalize features
preprocessed_data.to_csv("data/preprocessed_song_data.csv", index=False)
