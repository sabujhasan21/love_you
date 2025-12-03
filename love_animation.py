import streamlit as st

st.set_page_config(page_title="❤️ Love Gift Animation ❤️", layout="wide")

st.markdown("""
<style>
html, body, [class*="block-container"] {
    margin:0; padding:0; overflow:hidden; height:100vh; width:100vw;
    background: linear-gradient(to bottom right, #1a0f1f, #4d0f1f);
}

#container {
    width:100%; height:100%; position:relative; text-align:center;
    overflow:hidden;
}

#gift {
    font-size:15vh; cursor:pointer; position:absolute; top:50%; left:50%;
    transform:translate(-50%, -50%);
}

#open-text {
    position:absolute; top:60%; left:50%; transform:translateX(-50%);
    font-size:3vh; color:#ffe6f2; font-family:Georgia, serif;
}

.message {
    position:absolute; top:50%; left:50%; transform:translate(-50%, -50%);
    color:#ffe6f2; font-family:Georgia, serif; font-size:4vh;
    text-align:center;
}

.final {
    position:absolute; top:50%; left:50%; transform:translate(-50%, -50%);
    font-family:Georgia, serif; font-size:8vh; color:#ff4d6d; text-align:center;
}

.heart {
    position:absolute; font-size:20px; color:transparent; -webkit-text-stroke:1px #ff4d6d;
    user-select:none;
}
</style>

<div id="container">
    <div id="gift">💝</div>
    <div id="open-text">Open the box</div>
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

function createHeart() {
    const heart = document.createElement('div');
    heart.classList.add('heart');
    heart.innerText = "❤️";
    heart.style.left = Math.random()*95 + "%";
    heart.style.top = "-5%";
    heart.style.fontSize = (15 + Math.random()*15) + "px";
    container.appendChild(heart);
    hearts.push({el:heart, speed:1+Math.random()*2});
}

function animateHearts() {
    hearts.forEach((h,i)=>{
        let top = parseFloat(h.el.style.top);
        top += h.speed;
        if(top>100) {
            container.removeChild(h.el);
            hearts.splice(i,1);
            createHeart();
        } else {
            h.el.style.top = top + "%";
        }
    });
    requestAnimationFrame(animateHearts);
}

animateHearts();
for(let i=0;i<50;i++){createHeart();}

gift.addEventListener('click', ()=>{
    gift.style.display='none';
    openText.style.display='none';
    let idx=0;
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message');
    container.appendChild(messageDiv);

    function typeWriter(msg, cb){
        let i=0;
        messageDiv.innerText="";
        function type(){
            if(i<msg.length){
                messageDiv.innerText += msg[i];
                i++;
                setTimeout(type,50);
            } else {
                setTimeout(cb,1500);
            }
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
        }
    }

    // Gift burst hearts
    for(let i=0;i<100;i++){
        const b = document.createElement('div');
        b.classList.add('heart');
        b.innerText="❤️";
        b.style.left = 50 + Math.random()*10 -5 + "%";
        b.style.top = 50 + Math.random()*10 -5 + "%";
        b.style.fontSize = (10 + Math.random()*20) + "px";
        container.appendChild(b);
        hearts.push({el:b, speed:Math.random()*3 +1});
    }

    nextMessage();
});
</script>
""", unsafe_allow_html=True)
