import requests
from io import BytesIO
import json
from PIL import Image, ImageDraw, ImageFont
from preprocessing import get_dominant_color, create_gradient, get_fitting_font

def generate_spotify_poster(data):
    """Generate an A4-sized Spotify track poster from track data."""

    def json_fix(data):
        return json.loads(json.dumps(data), parse_constant=lambda x: None)

    data = json_fix(data)    # A4 dimensions in pixels (300 DPI)
    a4_width, a4_height = 2480, 3508
    a4_image = Image.new("RGB", (a4_width, a4_height), "white")

    # Fetch the track image from URL
    response = requests.get(data['album']['images'][0]['url'])
    track_art = Image.open(BytesIO(response.content))

    # Define gradient colors
    end_color = get_dominant_color(track_art)
    start_color = (255, 255, 255)  # White

    # Create and blend gradient
    gradient = create_gradient(a4_width, a4_height, start_color, end_color)
    a4_image = Image.blend(a4_image.convert("RGBA"), gradient.convert("RGBA"), alpha=0.6)

    # Resize and center track art
    track_art_size = 2300
    track_art = track_art.resize((track_art_size, track_art_size))
    x_position = (a4_width - track_art_size) // 2
    y_position = 90
    a4_image.paste(track_art, (x_position, y_position))

    # Load fonts
    font_path1 = "components/Lexend_Deca/static/LexendDeca-SemiBold.ttf"
    font_path2 = "components/Lexend_Deca/static/LexendDeca-Medium.ttf"

    # Draw text
    draw = ImageDraw.Draw(a4_image)
    max_text_width = a4_width - 180  # Keep some margin

    # Dynamically adjusted fonts
    font1 = get_fitting_font(font_path1, data['name'], max_text_width, draw)
    font2 = get_fitting_font(font_path2, data['album']['artists'][0]['name'], max_text_width, draw, initial_size=128)
    # font2 = ImageFont.truetype(font_path2, 128)  # Smaller font for artist name

    # Track Name
    track_name = data['name']
    text_bbox = draw.textbbox((0, 0), track_name, font=font1, anchor="lt")
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (a4_width - text_width) // 2
    text_y = 2390
    draw.text((text_x, text_y), track_name, fill=end_color, font=font1)

    # Artist Name
    artist_name = data['album']['artists'][0]['name']
    artist_bbox = draw.textbbox((0, 0), artist_name, font=font2, anchor="lt")
    artist_width = artist_bbox[2] - artist_bbox[0]
    artist_x = (a4_width - artist_width) // 2
    artist_y = text_y + text_height + 80
    draw.text((artist_x, artist_y), artist_name, fill="black", font=font2)

    # Load and paste PNG components
    png_path = "components/layout.png"
    shape_image = Image.open(png_path).convert("RGBA")
    shape_width, shape_height = shape_image.size
    shape_x = (a4_width - shape_width) // 2
    shape_y = 2920
    a4_image.paste(shape_image, (shape_x, shape_y), shape_image)

    return a4_image

