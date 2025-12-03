import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="❤️ Love Gift Animation ❤️", layout="wide")

html_code = """
<style>
html, body, [class*="block-container"] {
    margin:0; padding:0; overflow:hidden; height:100vh; width:100vw;
    background: radial-gradient(circle at center, #1a0f1f, #4d0f1f 100%);
}

#container {
    width:100%; height:100%; position:relative; text-align:center; overflow:hidden;
}

#gift {
    font-size:15vh; cursor:pointer; position:absolute; top:50%; left:50%;
    transform:translate(-50%, -50%); transition: transform 0.3s ease;
}

#open-text {
    position:absolute; top:60%; left:50%; transform:translateX(-50%);
    font-size:3vh; color:#ffe6f2; font-family:Georgia, serif;
}

.message {
    position:absolute; top:50%; left:50%; transform:translate(-50%, -50%);
    color:#ffe6f2; font-family:Georgia, serif; font-size:4vh;
    text-align:center; opacity:0; transition: opacity 1s ease;
}

.final {
    position:absolute; top:50%; left:50%; transform:translate(-50%, -50%);
    font-family:Georgia, serif; font-size:8vh; color:#ff4d6d;
    text-align:center; opacity:0; transition: opacity 2s ease;
}

.heart {
    position:absolute; font-size:15px; color:transparent; -webkit-text-stroke:1px #ff4d6d;
    user-select:none; will-change: transform, top, opacity;
}

.star {
    position:absolute; width:2px; height:2px; background:white;
    border-radius:50%; opacity:0.8;
    animation: twinkle 2s infinite alternate;
}

@keyframes twinkle {
    from { opacity: 0.2; transform: scale(0.5); }
    to { opacity: 1; transform: scale(1.2); }
}
</style>

<div id="container">
    <div id="gift">💝</div>
    <div id="open-text">Open the box</div>
    <audio autoplay loop>
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
    </audio>
</div>

<script>
const container = document.getElementById('container');
const gift = document.getElementById('gift');
const openText = document.getElementById('open-text');

const messages = [
"My heart smiles whenever I think of you.",
"You are the sweetest part of my life.",
"Every moment with you feels like magic.",
"You make my ordinary days feel special.",
"Your love is the reason I believe in happiness.",
"You are my peace, my joy, my everything.",
"My world feels complete because of you.",
"And lastly..."
];

let hearts = [];
let stars = [];

// Create stars
for(let i=0;i<80;i++){
    const s = document.createElement('div');
    s.classList.add('star');
    s.style.left=Math.random()*100+"%";
    s.style.top=Math.random()*100+"%";
    s.style.width=(1+Math.random()*2)+"px";
    s.style.height=(1+Math.random()*2)+"px";
    s.style.animationDuration=(1+Math.random()*3)+"s";
    container.appendChild(s);
    stars.push(s);
}

// Floating stroke hearts
function createHeart(size=15, top=-5, x=null){
    const heart = document.createElement('div');
    heart.classList.add('heart');
    heart.innerText="❤️";
    heart.style.left = (x!==null ? x : Math.random()*95) + "%";
    heart.style.top = top + "%";
    heart.style.fontSize = size + "px";
    heart.rotation = Math.random()*360;
    heart.speed = 0.05 + Math.random()*0.2;  // slower
    heart.alpha = 0;
    container.appendChild(heart);
    hearts.push(heart);
}

function animateHearts(){
    hearts.forEach((h,i)=>{
        let top = parseFloat(h.style.top);
        top += h.speed;
        h.style.top = top + "%";
        h.rotation += 0.2; // slower rotation
        h.style.transform = "translate(-50%,0) rotate("+h.rotation+"deg)";
        h.alpha += 0.002; // slow fade-in
        if(h.alpha>1) h.alpha=1;
        h.style.opacity = h.alpha;
        if(top>100){
            container.removeChild(h);
            hearts.splice(i,1);
            createHeart();
        }
    });
    requestAnimationFrame(animateHearts);
}

for(let i=0;i<50;i++){ createHeart(); }
animateHearts();

// Gift click
gift.addEventListener('click', ()=>{
    gift.style.transform="translate(-50%,-50%) scale(0)";
    setTimeout(()=>{gift.style.display='none'; openText.style.display='none';},300);

    // Small stroke heart bursts
    for(let i=0;i<80;i++){
        createHeart(Math.random()*12+8, 50+Math.random()*10, 50+Math.random()*10);
    }

    let idx=0;
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message');
    container.appendChild(messageDiv);

    function typeWriter(msg, cb){
        let i=0;
        messageDiv.innerText="";
        messageDiv.style.opacity=1;
        function type(){
            if(i<msg.length){
                messageDiv.innerText += msg[i];
                if(msg[i]===' ') messageDiv.innerText += '\u00A0'; 
                i++;
                setTimeout(type,70); // slower typing
            } else { setTimeout(cb,1800); }
        }
        type();
    }

    function nextMessage(){
        if(idx<messages.length){
            typeWriter(messages[idx], nextMessage);
            idx++;
        } else {
            container.removeChild(messageDiv);
            const finalDiv = document.createElement('div');
            finalDiv.classList.add('final');
            finalDiv.innerText="I love you, Sona ❤️";
            container.appendChild(finalDiv);
            setTimeout(()=>{finalDiv.style.opacity=1;},100);
        }
    }

    nextMessage();
});
</script>
"""

html(html_code, height=900)
