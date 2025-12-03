import streamlit as st
import time
import random

st.set_page_config(page_title="❤️ Love Gift Animation ❤️", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
html, body, [class*="block-container"] {
    margin:0;
    padding:0;
    overflow:hidden;
    height:100vh;
    width:100vw;
    background: linear-gradient(to bottom right, #1a0f1f, #4d0f1f);
}

#hearts-container {
    position: absolute;
    width: 100%;
    height: 100%;
    pointer-events: none;
    overflow: hidden;
}

.heart {
    position: absolute;
    font-size: 20px;
    color: transparent;
    -webkit-text-stroke: 1px #ff4d6d;
    user-select: none;
    animation: fall linear forwards;
}

@keyframes fall {
    0% {transform: translateY(-10px);}
    100% {transform: translateY(100vh);}
}

.center-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: #ffe6f2;
    font-family: Georgia, serif;
    text-align: center;
    font-size: 4vh;
}

.final-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-family: Georgia, serif;
    font-size: 8vh;
    color: #ff4d6d;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------- Hearts HTML ----------
hearts_html = '<div id="hearts-container">'
for _ in range(50):
    x = random.randint(0, 95)
    delay = random.uniform(0, 5)
    size = random.randint(15, 30)
    speed = random.uniform(5, 12)
    hearts_html += f'''
    <div class="heart" style="left:{x}%; font-size:{size}px; animation-duration:{speed}s; animation-delay:{delay}s;">❤️</div>
    '''
hearts_html += '</div>'
st.markdown(hearts_html, unsafe_allow_html=True)

# ---------- Placeholders ----------
gift_placeholder = st.empty()
message_placeholder = st.empty()
final_placeholder = st.empty()

# ---------- Gift Box ----------
with gift_placeholder.container():
    st.markdown(
        '<div class="center-text"><h1 style="font-size:15vh; cursor:pointer;" id="gift">💝</h1>'
        '<div style="font-size:3vh;">Open the box</div></div>',
        unsafe_allow_html=True
    )
    open_gift = st.button("Open the Gift 💝")

# ---------- Typewriter Function ----------
def typewriter(msg, placeholder, delay=0.05):
    text = ""
    for char in msg:
        text += char
        placeholder.markdown(f'<div class="center-text">{text}</div>', unsafe_allow_html=True)
        time.sleep(delay)

# ---------- On Gift Click ----------
if open_gift:
    gift_placeholder.empty()

    # Sequential romantic messages (typewriter)
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
        typewriter(msg, message_placeholder)
        time.sleep(1.5)  # small pause between messages

    message_placeholder.empty()

    # ---------- Final Text ----------
    final_placeholder.markdown(
        '<div class="final-text">I love you, Sona ❤️</div>',
        unsafe_allow_html=True
    )
