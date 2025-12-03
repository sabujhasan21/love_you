import streamlit as st
import time
import random

# Page setup
st.set_page_config(layout="wide")
st.title("💖 Love Animation 💖")

# Background
st.markdown(
    """
    <style>
    .bg {
        background-image: linear-gradient(to bottom right, #ffb6c1, #ffc0cb);
        height: 100vh;
        background-size: cover;
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
        text-align: center;
        margin-top: 150px;
    }
    .instruction {
        text-align: center;
        font-size: 24px;
        color: #fff;
    }
    </style>
    <div class="bg">
        <div class="gift">
            <h1 style="font-size:120px; cursor:pointer;">💝</h1>
            <div class="instruction">Open the gift</div>
        </div>
    </div>
    """, 
    unsafe_allow_html=True
)

# Placeholder for messages
message_placeholder = st.empty()
final_placeholder = st.empty()

# Button to trigger gift opening
gift_clicked = st.button("Open the Gift 💝")

if gift_clicked:
    # Show gift-blast effect (hearts around)
    hearts_html = ""
    for _ in range(30):
        x = random.randint(0, 90)
        y = random.randint(0, 80)
        size = random.randint(20, 40)
        hearts_html += f'<div class="heart" style="left:{x}%; top:{y}%; font-size:{size}px;">❤️</div>'
    st.markdown(hearts_html, unsafe_allow_html=True)

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
            f"<h2 style='text-align:center; color:#fff; font-family:sans-serif'>{msg}</h2>", 
            unsafe_allow_html=True
        )
        time.sleep(2)

    # Clear messages and show final message
    message_placeholder.empty()
    final_placeholder.markdown(
        "<h1 style='text-align:center; font-size:80px; color:#ff4d6d;'>I love you, Sona ❤️</h1>", 
        unsafe_allow_html=True
    )
