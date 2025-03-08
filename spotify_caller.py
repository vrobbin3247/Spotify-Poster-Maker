import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st

SPOTIFY_CLIENT_ID = st.secrets["spotify"]["client_id"]
SPOTIFY_CLIENT_SECRET = st.secrets["spotify"]["client_secret"]

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))


def get_track_data(track_url):
    """Fetch track details from Spotify API using a track URL."""

    # Extract track ID from URL
    track_id = track_url.split("/")[-1].split("?")[0]

    # Fetch track details
    track_data = sp.track(track_id)

    # Extract relevant details
    track_info = {
        "name": track_data["name"],
        "album": {
            "name": track_data["album"]["name"],
            "release_date": track_data["album"]["release_date"],
            "images": track_data["album"]["images"],  # List of album art (different sizes)
            "artists": [{"name": artist["name"]} for artist in track_data["album"]["artists"]]
        }
    }

    return track_info
