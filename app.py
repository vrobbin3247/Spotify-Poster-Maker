import streamlit as st
from poster_maker import generate_spotify_poster
from spotify_caller import get_track_data
import re
from io import BytesIO


# Regex pattern for Spotify track URLs
SPOTIFY_TRACK_PATTERN = r"https?://open\.spotify\.com/track/[a-zA-Z0-9]+"

st.title("Spotify Poster Generator 🎵")

# Get user input
url = st.text_input('Enter a Spotify track URL')

if url:
    #Check if URL is correctly formatted
    if not re.match(SPOTIFY_TRACK_PATTERN, url):
        st.error("❌ Invalid Spotify track URL! Please enter a valid Spotify track link.")
    else:
        try:
            #Try fetching track data
            data = get_track_data(url)

            if not data:  # If the response is empty or invalid
                st.error("⚠️ No track data found. Please enter a valid Spotify track URL.")
            else:
                # Generate and display the poster
                image = generate_spotify_poster(data)
                st.image(image)
                img_buffer = BytesIO()
                image.save(img_buffer, format="png")
                img_bytes = img_buffer.getvalue()

                # st.markdown(
                #     """
                #     <style>
                #     .stDownloadButton button {
                #         background-color: #FF5733 !important; /* Custom color */
                #     }
                #     </style>
                #     """,
                #     unsafe_allow_html=True,
                # )

                st.download_button(
                    label="Download Poster",
                    data=img_bytes,
                    file_name="poster.png",
                    mime="image/jpeg",
                    icon=":material/download:",
                )

        except Exception as e:
            st.error(f"❌ Error fetching track data: {str(e)}")