import streamlit as st

st.set_page_config(
    page_title="הפרוייקט של לביא 🔥",
    page_icon="🚀",
    layout="wide"
)

# ───── CSS אנימציות מגניבות 🔥 ─────
st.markdown("""
<style>
/* רקע גרדיאנט זז מטורף */
@keyframes bgMove {
  0% {background-position: 0% 50%;}
  50% {background-position: 100% 50%;}
  100% {background-position: 0% 50%;}
}
body {
    background: linear-gradient(120deg, #ff9a9e, #fad0c4, #a1c4fd, #c2e9fb);
    background-size: 300% 300%;
    animation: bgMove 30s ease infinite;
    font-family: 'Arial', sans-serif;
    overflow-x: hidden;
}

/* קונטיינר דינאמי */
.main-box {
    background: rgba(255,255,255,0.9);
    width: 80%;
    margin: auto;
    padding: 50px;
    border-radius: 25px;
    box-shadow: 0 0 35px rgba(0,0,0,0.2);
    text-align: center;
    transition: transform 0.5s ease, box-shadow 0.5s ease;
}
.main-box:hover {
    transform: scale(1.03) rotate(-1deg);
    box-shadow: 0 0 55px rgba(0,0,0,0.35);
}

/* כותרת pulsate מטורפת */
@keyframes pulseBig {
  0% { transform: scale(1); color: #0e4d8a; text-shadow: 0 0 15px rgba(0,0,0,0.2);}
  50% { transform: scale(1.08); color: #ff6a00; text-shadow: 0 0 25px rgba(255,105,0,0.7);}
  100% { transform: scale(1); color: #0e4d8a; text-shadow: 0 0 15px rgba(0,0,0,0.2);}
}
.title {
    font-size: 60px;
    font-weight: bold;
    animation: pulseBig 3s infinite;
    margin-bottom: 20px;
}

/* תת כותרת עם fadeIn */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px);}
  to { opacity: 1; transform: translateY(0);}
}
.subtitle {
    font-size: 24px;
    color: #333;
    margin-bottom: 40px;
    animation: fadeInUp 2s ease forwards;
    opacity: 0;
}

/* כפתור mega 🔥 */
.stButton>button {
    background-color: #ff3c3c;
    color: white;
    padding: 16px 38px;
    font-size: 20px;
    border-radius: 18px;
    font-weight: bold;
    border: none;
    transition: transform 0.4s, box-shadow 0.4s, background-color 0.4s;
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}
.stButton>button:hover {
    transform: scale(1.15) rotate(-3deg);
    box-shadow: 0 15px 45px rgba(0,0,0,0.45);
    background-color: #ff1a1a;
}

/* כרטיסים מטורפים floating + rotate */
@keyframes floatRotate {
  0% { transform: translateY(0px) rotate(0deg);}
  25% { transform: translateY(-10px) rotate(-2deg);}
  50% { transform: translateY(0px) rotate(0deg);}
  75% { transform: translateY(10px) rotate(2deg);}
  100% { transform: translateY(0px) rotate(0deg);}
}
.card {
    background: linear-gradient(135deg, #ffe29f, #ff719a);
    padding: 22px;
    border-radius: 20px;
    box-shadow: 0 0 18px rgba(0,0,0,0.15);
    font-size: 20px;
    margin-bottom: 25px;
    animation: floatRotate 4s ease-in-out infinite;
    transition: transform 0.3s, box-shadow 0.3s;
}
.card:hover {
    transform: scale(1.12) rotate(-5deg);
    box-shadow: 0 0 45px rgba(0,0,0,0.35);
}

/* אנימציית לבבות ברקע 🌸 */
@keyframes hearts {
    0% {transform: translateY(0) rotate(0deg);}
    50% {transform: translateY(-15px) rotate(15deg);}
    100% {transform: translateY(0) rotate(0deg);}
}
.heart {
    display:inline-block;
    font-size: 28px;
    animation: hearts 2s infinite;
}
.heart:nth-child(2) { animation-delay: 0.2s; }
.heart:nth-child(3) { animation-delay: 0.4s; }
.heart:nth-child(4) { animation-delay: 0.6s; }
.heart:nth-child(5) { animation-delay: 0.8s; }
</style>
""", unsafe_allow_html=True)

# ───── דף הבית 🔥 ─────
st.markdown("<div class='main-box'>", unsafe_allow_html=True)

# כותרת עם אנימציות
st.markdown("<div class='title'>ברוך הבא לפרוייקט של לביא 🔥</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>צבעים מטורפים, אנימציות מגניבות וכרטיסים זזים 🌈</div>", unsafe_allow_html=True)

# לבבות זזים מעל הכפתור
st.markdown("<div class='heart'>❤️</div><div class='heart'>💛</div><div class='heart'>💚</div><div class='heart'>💙</div><div class='heart'>💜</div>", unsafe_allow_html=True)

if st.button("👦 מעבר לעמוד של אליאס"):
    st.switch_page("pages/alies.py")
if st.button("👦 מעבר לעמוד של השיעורי הבית"):
    st.switch_page("Pages/homework.py")

st.markdown("</div>", unsafe_allow_html=True)

