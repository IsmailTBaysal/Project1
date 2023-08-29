"""
 Define data models and structures.
"""
class Song:
    def __init__(self, title, artist, genre, features):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.features = features

    def __str__(self):
        return f"{self.title} by {self.artist}"

    # The features of the song.
    def get_features(self):
        return self.features