import streamlit as st
import time
import os

# Page setup
st.set_page_config(layout="wide")
st.title("💖 Love Animation 💖")

# Absolute path for music file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
music_path = os.path.join(BASE_DIR, "music", "bg_music.mp3")

# Background music
st.audio(music_path, format="audio/mp3", start_time=0)

# Gift box emoji
st.markdown(
    "<h1 style='text-align:center; font-size:120px; cursor:pointer;'>💝</h1>", 
    unsafe_allow_html=True
)
st.markdown(
    "<h3 style='text-align:center;'>Click the gift to open</h3>", 
    unsafe_allow_html=True
)

# Placeholders for messages and final message
message_placeholder = st.empty()
final_placeholder = st.empty()

# Button to trigger gift opening
gift_clicked = st.button("Open the Gift 💝")

if gift_clicked:
    # Show gift opening animation (simple text effect)
    st.markdown("<h1 style='text-align:center; font-size:120px; color:#ff4d6d;'>💝</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Opening...</h3>", unsafe_allow_html=True)
    time.sleep(1)

    # Sequential messages
    messages = [
        "My heart smiles whenever I think of you.",
        "You are the sweetest part of my life.",
        "Every moment with you feels like magic.",
        "You make my ordinary days feel special.",
        "Your love is the reason I believe in happiness.",
        "You are my peace, my joy, my everything.",
        "My world feels complete because of you.",
        "And lastly..."
    ]

    for msg in messages:
        message_placeholder.markdown(
            f"<h2 style='text-align:center; color:#ffe6f2'>{msg}</h2>", 
            unsafe_allow_html=True
        )
        time.sleep(2)  # delay between messages

    # Clear messages and show final romantic message
    message_placeholder.empty()
    final_placeholder.markdown(
        "<h1 style='text-align:center; font-size:80px; color:#ff4d6d;'>I love you, Sona ❤️</h1>", 
        unsafe_allow_html=True
    )
