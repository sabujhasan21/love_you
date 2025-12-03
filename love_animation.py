import streamlit as st
import time
import random

# Page setup
st.set_page_config(layout="wide")

# Romantic background using CSS
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom right, #ffb6c1, #ffc0cb);
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
</style>
""", unsafe_allow_html=True)

# Display gift box + instruction
st.markdown(
    """
    <div class="gift">
        <h1 style='font-size:120px; cursor:pointer;'>💝</h1>
        <div class="instruction">Open the gift</div>
    </div>
    """, unsafe_allow_html=True
)

# Placeholders
message_placeholder = st.empty()
final_placeholder = st.empty()

# Button to trigger gift opening
gift_clicked = st.button("Open the Gift 💝")

if gift_clicked:
    # Gift-blast hearts effect
    hearts_html = ""
    for _ in range(30):
        x = random.randint(0, 90)
        y = random.randint(0, 80)
        size = random.randint(20, 40)
        hearts_html += f'<div class="heart" style="left:{x}%; top:{y}%; font-size:{size}px;">❤️</div>'
    st.markdown(hearts_html, unsafe_allow_html=True)

    # Sequential romantic messages
    messages = [
        "Dear, my love...",
        "You fill my life with happiness.",
        "Every moment with you is magical.",
        "You are my sweetest joy.",
        "You make my heart flutter.",
        "My world shines because of you.",
        "I cherish you forever.",
        "And finally..."
    ]

    for msg in messages:
        message_placeholder.markdown(
            f"<h2 style='text-align:center; color:#ffe6f2'>{msg}</h2>", unsafe_allow_html=True
        )
        time.sleep(2)

    # Clear messages and show final romantic message
    message_placeholder.empty()
    final_placeholder.markdown(
        "<h1 style='text-align:center; font-size:80px; color:#ff4d6d;'>I love you, Sona ❤️</h1>",
        unsafe_allow_html=True
    )
