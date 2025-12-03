~~~{"id":"83422","variant":"standard"}
import streamlit as st

st.set_page_config(layout="wide", page_title="❤️ Love Gift Animation ❤️")

# ----- HTML + JS + CSS -----
st.markdown("""
<audio autoplay loop>
  <source src="bg_music.mp3" type="audio/mpeg">
</audio>

<style>
.main {
  background: linear-gradient(120deg, #1a0f1f, #3a0b32, #1a0f1f);
  height: 100vh;
  color: white;
  overflow: hidden;
}
#gift {
  font-size: 120px;
  text-align:center;
  cursor:pointer;
}
#text_area {
  font-family: Georgia, serif;
  text-align:center;
  font-size: 36px;
  margin-top:20px;
}
.heart {
  position: absolute;
  color: #ff4d6d;
  font-size: 24px;
  animation: float 8s linear infinite;
}
@keyframes float {
  0% {transform: translateY(0px);}
  50% {transform: translateY(-200px);}
  100% {transform: translateY(0px);}
}
</style>

<div class="main">
  <div id="gift">💝</div>
  <div id="text_area">Open the box</div>
  <div id="hearts"></div>
</div>

<script>
let gift = document.getElementById("gift");
let text_area = document.getElementById("text_area");
let hearts_div = document.getElementById("hearts");
gift.onclick = function() {
  gift.style.display="none";
  text_area.style.display="none";

  // Heart burst
  for(let i=0;i<50;i++){
    let h = document.createElement("div");
    h.className="heart";
    h.style.left=Math.random()*window.innerWidth+"px";
    h.style.top=Math.random()*window.innerHeight+"px";
    h.style.fontSize=(12+Math.random()*24)+"px";
    hearts_div.appendChild(h);
  }

  // Typewriter messages
  let messages = [
    "My heart smiles whenever I think of you.",
    "You are the sweetest part of my life.",
    "Every moment with you feels like magic.",
    "You make my ordinary days feel special.",
    "Your love is the reason I believe in happiness.",
    "You are my peace, my joy, my everything.",
    "My world feels complete because of you.",
    "And lastly..."
  ];

  let index=0;
  let charIndex=0;
  let textEl = document.createElement("div");
  textEl.style.fontSize="48px";
  textEl.style.fontFamily="Georgia, serif";
  textEl.style.textAlign="center";
  textEl.style.marginTop="20px";
  document.body.appendChild(textEl);

  function typeMessage(){
    if(index>=messages.length){
      setTimeout(()=>{
        // Final text
        let final = document.createElement("div");
        final.innerHTML="I love you, Sona ❤️";
        final.style.fontSize="72px";
        final.style.fontFamily="Georgia, serif";
        final.style.color="#ff4d6d";
        final.style.textAlign="center";
        final.style.marginTop="50px";
        document.body.appendChild(final);
      },500);
      return;
    }
    if(charIndex<=messages[index].length){
      textEl.innerHTML=messages[index].substring(0,charIndex);
      charIndex++;
      setTimeout(typeMessage,80);
    }else{
      charIndex=0;
      index++;
      setTimeout(typeMessage,2000);
    }
  }
  typeMessage();
};
</script>
""", unsafe_allow_html=True)
