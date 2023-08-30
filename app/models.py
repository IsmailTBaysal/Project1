"""
 Define data models and structures.
"""


class Song:
    def __init__(self, title, artist, genre, features):
        self.title = title
        self.artist = artist
        self.genre = genre
        self._features = features

    def __str__(self):
        return f"{self.title} by {self.artist}"

    def get_features(self):
        return self._features

    def set_features(self, features):
        self._features = features
