# love_animation.py
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("💖 Love Animation 💖")

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
body {
    margin:0;
    overflow:hidden;
    background: linear-gradient(#1a0f1f,#330022);
    font-family: Georgia, serif;
    color:white;
}
#gift {
    position:absolute;
    top:40%;
    left:50%;
    transform:translate(-50%, -50%);
    font-size:120px;
    cursor:pointer;
}
#instruction {
    position:absolute;
    top:55%;
    left:50%;
    transform:translate(-50%, -50%);
    font-size:28px;
    color:#ffe6f2;
}
#message {
    position:absolute;
    top:50%;
    left:50%;
    transform:translate(-50%, -50%);
    font-size:36px;
    text-align:center;
}
#final {
    position:absolute;
    top:50%;
    left:50%;
    transform:translate(-50%, -50%);
    font-size:72px;
    color:#ff4d6d;
    opacity:0;
}
canvas {
    position:absolute;
    top:0;
    left:0;
}
</style>
</head>
<body>

<audio id="bgm" src="music/bg_music.mp3" autoplay loop></audio>

<div id="gift">💝</div>
<div id="instruction">Open the box</div>
<div id="message"></div>
<div id="final">I love you, Sona ❤️</div>
<canvas id="canvas"></canvas>

<script>
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let petals = [];
let explosions = [];
const NUM_PETALS = 50;

class Petal {
    constructor(){
        this.x = Math.random()*canvas.width;
        this.y = Math.random()*-canvas.height;
        this.size = Math.random()*10 + 6;
        this.speed = Math.random()*1.5+1;
        this.phase = Math.random()*2*Math.PI;
        this.swing = Math.random()*40+20;
    }
    update(){
        this.phase += 0.02;
        this.x += Math.sin(this.phase)*0.5;
        this.y += this.speed;
        if(this.y>canvas.height+10) this.y = -10;
    }
    draw(){
        ctx.beginPath();
        ctx.strokeStyle="#ff4d6d";
        ctx.lineWidth=2;
        const s = this.size/10;
        ctx.moveTo(this.x, this.y);
        for(let t=0; t<=360; t+=12){
            let rad = t*Math.PI/180;
            let px = 16*Math.pow(Math.sin(rad),3);
            let py = 13*Math.cos(rad)-5*Math.cos(2*rad)-2*Math.cos(3*rad)-Math.cos(4*rad);
            ctx.lineTo(this.x+px*s, this.y-py*s);
        }
        ctx.stroke();
    }
}
for(let i=0;i<NUM_PETALS;i++) petals.push(new Petal());

class Particle{
    constructor(x,y){
        this.x=x;
        this.y=y;
        const angle = Math.random()*2*Math.PI;
        const speed = Math.random()*3+2;
        this.dx = Math.cos(angle)*speed;
        this.dy = Math.sin(angle)*speed;
        this.size = Math.random()*10+6;
        this.life = 50;
    }
    update(){
        this.x += this.dx;
        this.y += this.dy;
        this.size *=0.95;
        this.life--;
    }
    draw(){
        ctx.beginPath();
        ctx.fillStyle="#ff4d6d";
        ctx.arc(this.x,this.y,this.size/2,0,2*Math.PI);
        ctx.fill();
    }
}

function animate(){
    ctx.clearRect(0,0,canvas.width,canvas.height);
    petals.forEach(p=>{p.update(); p.draw();});
    explosions.forEach((e,i)=>{
        e.update();
        e.draw();
        if(e.life<=0) explosions.splice(i,1);
    });
    requestAnimationFrame(animate);
}
animate();

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
let msgIndex=0;
let charIndex=0;
const msgDiv = document.getElementById("message");

function typeWriter(){
    if(msgIndex>=messages.length){
        document.getElementById("final").style.transition="opacity 3s";
        document.getElementById("final").style.opacity=1;
        msgDiv.innerHTML="";
        return;
    }
    const currentMsg = messages[msgIndex];
    msgDiv.innerHTML = currentMsg.slice(0,charIndex);
    charIndex++;
    if(charIndex>currentMsg.length){
        charIndex=0;
        msgIndex++;
        setTimeout(typeWriter,2500);
    }else{
        setTimeout(typeWriter,50);
    }
}

document.getElementById("gift").addEventListener("click",()=>{
    const gift = document.getElementById("gift");
    const instr = document.getElementById("instruction");
    const rect = gift.getBoundingClientRect();
    const x = rect.left + rect.width/2;
    const y = rect.top + rect.height/2;
    for(let i=0;i<30;i++) explosions.push(new Particle(x,y));
    gift.style.display="none";
    instr.style.display="none";
    typeWriter();
});
</script>
</body>
</html>
"""

components.html(html_code, height=900)
