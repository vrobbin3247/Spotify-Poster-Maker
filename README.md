# 🎵 Spotify Poster Maker

## 🚀 About the Project
Spotify Poster Maker is a simple **Streamlit** web app that generates a stylish **A4-sized poster** from a Spotify track URL. The poster features the track's **album art**, **artist name**, and a **gradient background** inspired by the dominant colors of the album cover.

## ✨ Features
- 🎨 **Gradient Background:** Extracts dominant color from album art and applies a gradient.
- 🖼️ **High-Quality Poster:** Generates an A4-sized image with a sleek design.
- 📝 **Dynamic Font Sizing:** Adjusts text size to fit the poster.
- 📥 **Download Option:** Save the generated poster as an image.
- 🔐 **Secure API Keys:** Uses **Streamlit Secrets** to store Spotify credentials.

## 🛠️ Setup and Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/spotify-poster-maker.git
cd spotify-poster-maker
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Spotify API Credentials
- Create a `secrets.toml` file inside the `.streamlit` directory.
- Add your **Spotify API keys**:
```toml
[spotify]
client_id = "your_client_id"
client_secret = "your_client_secret"
```

### 4️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

## 🎮 How to Use
1. **Enter a Spotify track URL** into the input box.
2. Click **Generate Poster** 🎨.
3. View your **custom poster**.
4. Click the **Download** button 📥 to save it!

## 🤝 Contributing
Contributions are **welcome**! Feel free to **fork** this repo and submit a **pull request**.

## 📜 License
This project is **MIT Licensed**.

---
🚀 *Made with ❤️ using Python, Streamlit & Spotipy* 🎶

