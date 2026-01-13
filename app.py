import streamlit as st
from streamlit_lottie import st_lottie
import requests
import google.generativeai as genai
import random

# --- Page Config ---
st.set_page_config(page_title="Sahil Desai | Portfolio",
                   layout="wide", page_icon="💼")
# --- Apply Theme CSS ---

# --- Theme Toggle ---
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"

theme_toggle = st.toggle("🌙(Dark Mode)", value=(
    st.session_state["theme"] == "dark"))
st.session_state["theme"] = "dark" if theme_toggle else "light"

# --- Apply Theme CSS ---


def apply_theme(theme):
    if theme == "dark":
        st.markdown("""
            <style>
                body, .stApp { background-color: #1e1e1e; color: #ffffff; }
                .css-18e3th9, .css-1d391kg { background-color: #262730; }
                h1, h2, h3, h4, h5, h6, p, li, ul { color: #ffffff !important; }
            </style>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                body, .stApp { background-color: #ffffff; color: #000000; }
                h1, h2, h3, h4, h5, h6, p, li, ul { color: #000000 !important; }
            </style>
            """, unsafe_allow_html=True)


apply_theme(st.session_state["theme"])

st.markdown("""
    <style>
    .fade-section {
        opacity: 0;
        transform: translateY(20px);
        animation: fadeInUp 1s ease-out forwards;
    }

    @keyframes fadeInUp {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    </style>
""", unsafe_allow_html=True)


# --- Gemini API Key (Do Not Edit This Block) ---
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
except Exception as e:
    st.error(f"Gemini API Key error: {e}")
    model = None

# --- Lottie Animation Loader ---


def load_lottie_url(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None
    return None


# --- Lottie Animations ---
lottie_hero = load_lottie_url(
    "https://assets10.lottiefiles.com/packages/lf20_touohxv0.json")  # Rocket launch
lottie_about = load_lottie_url(
    "https://assets2.lottiefiles.com/packages/lf20_4kx2q32n.json")
lottie_projects = load_lottie_url(
    "https://assets2.lottiefiles.com/packages/lf20_x1gjdldd.json")  # Projects
lottie_chatbot = load_lottie_url(
    "https://assets2.lottiefiles.com/packages/lf20_0yfsb3a1.json")  # Chatbot
lottie_footer = load_lottie_url(
    "https://assets2.lottiefiles.com/packages/lf20_3rwasyjy.json")   # Thank you


# --- Function to load Lottie animation ---

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Example Lottie animation (developer / person working)
lottie_person = load_lottieurl(
    "https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json")

# --- Hero Section ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
        <h1 style='font-size:2.8rem; font-family:Poppins;'>Hey, I'm <span style="background: linear-gradient(45deg, #6a11cb, #2575fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Sahil Desai 👋</span></h1>
        <h3 style='color:#c5c5c5;'>2nd Year BTech EXTC | VJTI Mumbai</h3>
        <p style='color:#dcdcdc;'>🚀 I’m passionate about <span style="color:#00b4d8;">Data Science</span>, <span style="color:#ff4d6d;">Machine Learning</span>, and <span style="color:#00b4d8;">DSA</span> — building smart systems that solve real-world problems.</p>
        <p style='color:#dcdcdc;'>💻 Currently working on <span style="color:#ff4d6d;">ML model building</span>, <span style="color:#00b4d8;">data visualization</span>, and <span style="color:#00b4d8;">algorithmic thinking</span> to sharpen my skills.</p>
        <p style='color:#dcdcdc;'>🧠 Exploring <span style="color:#00b4d8;">Competitive Programming</span> as a beginner — learning logic, problem-solving, and optimization step by step.</p>
        <p style='color:#dcdcdc;'>🎯 Always <span style="color:#ff4d6d;">learning by building</span>, pushing limits, and creating intelligent solutions 🚀</p>
    """, unsafe_allow_html=True)

with col2:
    if lottie_person:
        st_lottie(lottie_person, height=320, key="person")


if lottie_about:
    st_lottie(lottie_about, height=350, key="hero")  # close fade-section div


# --- About Me ---
with st.container():
    st.markdown("<div class='fade-section'>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
        .about-section h2 {
            font-family: 'Poppins', sans-serif;
            font-size: 32px;
            color: #FF4B4B;
        }
        .about-section p {
            font-family: 'Poppins', sans-serif;
            font-size: 17px;
            color: #999999;
            line-height: 1.6;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class="about-section">
    <h2>🧠 About Me</h2>
    <p>I'm a curious tech enthusiast who enjoys spending hours building and experimenting with projects that combine logic and creativity. Whether it's tinkering with ESP32 boards, exploring AI models, or improving my problem-solving skills — I love learning by doing.</p>
    <p>Offline, I’m a bit introverted and prefer quiet workspaces, but online I turn chatty — discussing ideas, tech, and memes alike 😄. I’m also a partial anime watcher (especially the thought-provoking ones) and enjoy discovering new tech tools and open-source projects.</p>
    <p>My hobbies revolve around exploring emerging tech, brainstorming project ideas, and occasionally losing track of time while debugging or watching coding podcasts.</p>
</div>

        """, unsafe_allow_html=True)
    with col2:
        if lottie_hero:
            st_lottie(lottie_hero, height=280, key="about")
    st.markdown("</div>", unsafe_allow_html=True)

# --- Projects Section ---
with st.container():
    st.markdown("<div class='fade-section'>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
        .projects-section h2 {
            font-family: 'Poppins', sans-serif;
            font-size: 32px;
            color: #FF4B4B;
            margin-bottom: 15px;
        }
        .project-box {
            font-family: 'Poppins', sans-serif;
            font-size: 17px;
            color: white;
            margin-bottom: 15px;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .box1 { background-color: #4CAF50; }   /* Green */
        .box2 { background-color: #FF9800; }   /* Orange */
        .box3 { background-color: #2196F3; }   /* Blue */

        .dark .box1, .dark .box2, .dark .box3 {
            filter: brightness(0.9);
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='projects-section'><h2>🛠️ Projects</h2></div>",
                unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("""
        <div class='project-box box1'>🤖 <b>Self-balancing Robot</b><br>
        Built using ESP32 and MPU6050 for real-time motion balancing and control.</div>

        <div class='project-box box2'>📊 <b>Smart Distance Monitoring System</b><br>
        ESP32-powered IoT setup with OLED display and live web visualization using Chart.js.</div>

        <div class='project-box box3'>🔍 <b>Fuzzy Name Search App</b><br>
        Streamlit-based app using fuzzy string matching for intelligent name lookups and similarity ranking.</div>
        """, unsafe_allow_html=True)

    with col2:
        if lottie_footer:
            st_lottie(lottie_footer, height=400, key="footer")
    st.markdown("</div>", unsafe_allow_html=True)

# --- Gemini Chatbot Section ---
with st.container():
    st.markdown("<div class='fade-section'>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
        .chatbot-title {
            font-family: 'Poppins', sans-serif;
            font-size: 32px;
            color: #FF4B4B;
            margin-bottom: 0.2em;
        }
        .chat-caption {
            font-family: 'Poppins', sans-serif;
            font-size: 16px;
            color: #666;
            margin-bottom: 20px;
        }
        .chatbot-box {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.07);
            font-family: 'Poppins', sans-serif;
            color: #333;
            margin-bottom: 20px;
        }
        .chatbot-response {
            background-color: #f4f4f4;
            padding: 15px;
            margin-top: 10px;
            border-left: 5px solid #FF4B4B;
            border-radius: 10px;
            font-family: 'Poppins', sans-serif;
        }
        .dark .chatbot-box {
            background-color: #1e1e24 !important;
            color: #dddddd !important;
        }
        .dark .chatbot-response {
            background-color: #2c2f35 !important;
            color: #e0e0e0 !important;
            border-left: 5px solid #4B8BBE;
        }
        .dark .chat-caption {
            color: #aaaaaa !important;
        }
        input[type="text"] {
            font-family: 'Poppins', sans-serif;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #cccccc;
            width: 100%;
        }
        </style>

        <div class='chatbot-title'>💬 Ask Me Anything About Sahil</div>
        <div class='chat-caption'>Curious about Sahil’s journey, projects, or achievements? Just ask!</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        # st.markdown("<div class='chatbot-box'>", unsafe_allow_html=True)
        user_input = st.text_input("🔎 Type your question here:")

        if user_input and model:
            with st.spinner("🤖 Thinking..."):
                prompt = f"""
    You are an AI assistant for Ganesh portfolio. Only reveal personal background info if asked directly.

    PRIVATE INFO (DO NOT reveal unless specifically asked):
    - Was a JEE student 2022-2024
    - Scored 84 ile in JEE Mains ,qualified JEE Advanced through EWS
    - Got 99.21 percentile in MHT-CET
    - Admitted to VJTI via EWS Quota in 2024
    - 7 CGPA in first year
    - Had a girlfriend in 12th (keep name private)

    User asked: {user_input}
    """
                try:
                    response = model.generate_content(prompt)
                    st.success(response.text)
                except Exception as e:
                    st.error(f"❌ AI response failed: {e}")

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        if lottie_chatbot:
            st_lottie(lottie_chatbot, height=280, key="chat")
    st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
with st.container():
    st.markdown("<div class='fade-section'>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<h2>✨ Thanks for Visiting!</h2>", unsafe_allow_html=True)
    st.write(
        "This portfolio is built with Python, Streamlit, and love for innovation.")
    if lottie_projects:
        st_lottie(lottie_projects, height=200, key="projects")
    st.markdown("</div>", unsafe_allow_html=True)
