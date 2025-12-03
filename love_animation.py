import streamlit as st
import time
import random

# ----- Page Config -----
st.set_page_config(page_title="❤️ Love Gift Animation ❤️", layout="wide")

# ----- CSS Styling -----
st.markdown("""
<style>
body {
    margin: 0;
    padding: 0;
    overflow: hidden;
    background: linear-gradient(to bottom right, #1a0f1f, #4d0f1f);
    height: 100vh;
}
.heart {
    position: absolute;
    font-size: 20px;
    animation: float 5s linear infinite;
}
@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-100px);}
    100% {transform: translateY(0px);}
}
.gift {
    position: absolute;
    top: 40%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    cursor: pointer;
}
.instruction {
    text-align: center;
    font-size: 28px;
    color: #ffe6f2;
    font-family: Georgia, serif;
}
.final {
    text-align: center;
    font-size: 80px;
    color: #ff4d6d;
    font-family: Georgia, serif;
}
</style>
""", unsafe_allow_html=True)

# ----- Floating Hearts Background -----
hearts_html = ""
for _ in range(50):
    x = random.randint(0, 90)
    y = random.randint(0, 80)
    size = random.randint(10, 30)
    hearts_html += f'<div class="heart" style="left:{x}%; top:{y}%; font-size:{size}px;">❤️</div>'
st.markdown(hearts_html, unsafe_allow_html=True)

# ----- Placeholders -----
gift_placeholder = st.empty()
message_placeholder = st.empty()
final_placeholder = st.empty()

# ----- Gift Box -----
with gift_placeholder.container():
    st.markdown(
        '<div class="gift"><h1 style="font-size:120px;">💝</h1>'
        '<div class="instruction">Open the box</div></div>',
        unsafe_allow_html=True
    )
    open_gift = st.button("Open the Gift 💝")

# ----- On Gift Click -----
if open_gift:
    gift_placeholder.empty()  # remove gift box

    # Heart explosion
    explosion_html = ""
    for _ in range(30):
        x = random.randint(30, 70)
        y = random.randint(30, 70)
        size = random.randint(20, 40)
        explosion_html += f'<div class="heart" style="left:{x}%; top:{y}%; font-size:{size}px;">❤️</div>'
    st.markdown(explosion_html, unsafe_allow_html=True)

    # Sequential romantic messages
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
            f'<h2 style="text-align:center; color:#ffe6f2; font-family:Georgia, serif;">{msg}</h2>',
            unsafe_allow_html=True
        )
        time.sleep(2)

    # Clear messages and show final text
    message_placeholder.empty()
    final_placeholder.markdown(
        '<div class="final">I love you, Sona ❤️</div>',
        unsafe_allow_html=True
    )
