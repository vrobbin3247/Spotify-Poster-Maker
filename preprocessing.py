import numpy as np
from PIL import Image, ImageDraw
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from PIL import Image, ImageDraw, ImageFont


def create_gradient(width, height, start_color, end_color):
    """Generate a vertical gradient image from start_color to end_color."""
    gradient = np.linspace(0, 1, height, dtype=np.float32)[:, None]  # Gradient values from 0 to 1
    start_rgb = np.array(start_color, dtype=np.float32)
    end_rgb = np.array(end_color, dtype=np.float32)

    gradient_rgb = (start_rgb * (1 - gradient) + end_rgb * gradient).astype(np.uint8)  # Interpolation
    gradient_image = np.repeat(gradient_rgb[:, np.newaxis, :], width, axis=1)  # Expand to full width
    return Image.fromarray(gradient_image)



def get_dominant_color(image, k=4):
    """Extract the dominant color from a PIL image or file path using K-Means clustering."""
    if isinstance(image, str):
        image = Image.open(image).convert("RGB")
    else:
        image = image.convert("RGB")

    image = image.resize((100, 100))  # Resize for faster processing
    pixels = np.array(image).reshape(-1, 3)

    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(pixels)

    dominant_color = kmeans.cluster_centers_[np.bincount(kmeans.labels_).argmax()]

    return tuple(map(int, dominant_color))  # Convert to (R, G, B)

def get_fitting_font(font_path, text, max_width, draw, initial_size=250, min_size=100):
    """Reduce font size dynamically until the text fits within the max_width."""
    font_size = initial_size
    while font_size >= min_size:
        font = ImageFont.truetype(font_path, font_size)
        text_width = draw.textbbox((0, 0), text, font=font, anchor="lt")[2]
        if text_width <= max_width:
            return font  # Return the first fitting font size
        font_size -= 10  # Decrease size step-by-step
    return ImageFont.truetype(font_path, min_size)