import streamlit as st
import requests
from streamlit_lottie import st_lottie
import google.generativeai as genai

# --------------------------------------------------
# PAGE CONFIG (MUST BE FIRST)
# --------------------------------------------------
st.set_page_config(
    page_title="Ganesh Sarode | Portfolio",
    page_icon="💼",
    layout="wide"
)

st.write("APP STARTED")  # Debug marker (remove later)

# --------------------------------------------------
# THEME
# --------------------------------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

dark_mode = st.toggle("🌙 Dark Mode", st.session_state.theme == "dark")
st.session_state.theme = "dark" if dark_mode else "light"


def apply_theme(theme):
    if theme == "dark":
        st.markdown("""
        <style>
        .stApp { background-color: #1e1e1e; color: white; }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        .stApp { background-color: white; color: black; }
        </style>
        """, unsafe_allow_html=True)


apply_theme(st.session_state.theme)

# --------------------------------------------------
# LOTTIE LOADER
# --------------------------------------------------
@st.cache_data
def load_lottie(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return r.json()
    except:
        return None
    return None


lottie_person = load_lottie(
    "https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json")
lottie_about = load_lottie(
    "https://assets2.lottiefiles.com/packages/lf20_4kx2q32n.json")
lottie_chat = load_lottie(
    "https://assets2.lottiefiles.com/packages/lf20_0yfsb3a1.json")

# --------------------------------------------------
# GEMINI SETUP (FAIL-SAFE)
# --------------------------------------------------
model = None
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception:
    st.warning("Gemini chatbot disabled (API key missing)")

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <h1>Hey, I'm <span style="color:#6a11cb;">Ganesh Sarode 👋</span></h1>
    <h3>BTech Student | Engineering Aspirant</h3>
    <p>Focused on Data Structures, Algorithms, and building real-world projects.</p>
    """, unsafe_allow_html=True)

with col2:
    if lottie_person:
        st_lottie(lottie_person, height=300)

st.divider()

# --------------------------------------------------
# ABOUT SECTION
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("🧠 About Me")
    st.write("""
    I’m a tech-focused student who believes in learning by building.
    I work on Python, DSA, and applied problem-solving.
    My goal is to convert strong fundamentals into real engineering skill.
    """)

with col2:
    if lottie_about:
        st_lottie(lottie_about, height=280)

st.divider()

# --------------------------------------------------
# PROJECTS
# --------------------------------------------------
st.subheader("🛠️ Projects")

st.success("🔍 Fuzzy Name Search App – Streamlit + Python")
st.info("🤖 Automation & AI-based Experiments")
st.warning("📊 Data Analysis & Visualization Projects")

st.divider()

# --------------------------------------------------
# CHATBOT
# --------------------------------------------------
st.subheader("💬 Ask Me Anything About Ganesh")

question = st.text_input("Type your question")

if question:
    if model:
        with st.spinner("Thinking..."):
            prompt = f"""
You are an AI assistant for Ganesh Sarode's portfolio.

User question: {question}
"""
            try:
                response = model.generate_content(prompt)
                st.success(response.text)
            except:
                st.error("AI failed to respond.")
    else:
        st.error("Chatbot unavailable (API key missing).")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()
st.write("✨ Built with Python & Streamlit")
