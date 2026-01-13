import streamlit as st
import requests
from streamlit_lottie import st_lottie
import google.generativeai as genai

# --------------------------------------------------
# PAGE CONFIG (FIRST STREAMLIT COMMAND)
# --------------------------------------------------
st.set_page_config(
    page_title="Ganesh Sarode | Portfolio",
    page_icon="💼",
    layout="wide"
)

# --------------------------------------------------
# DEBUG MARKER
# --------------------------------------------------
st.write("APP STARTED")

# --------------------------------------------------
# THEME TOGGLE
# --------------------------------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

dark_mode = st.toggle("🌙 Dark Mode", st.session_state.theme == "dark")
st.session_state.theme = "dark" if dark_mode else "light"


def apply_theme(theme):
    if theme == "dark":
        st.markdown(
            "<style>.stApp{background-color:#1e1e1e;color:white;}</style>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            "<style>.stApp{background-color:white;color:black;}</style>",
            unsafe_allow_html=True,
        )


apply_theme(st.session_state.theme)

# --------------------------------------------------
# SAFE LOTTIE LOADER
# --------------------------------------------------
@st.cache_data
def load_lottie(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return r.json()
    except Exception:
        return None
    return None


lottie_person = load_lottie(
    "https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json"
)

# --------------------------------------------------
# GEMINI SETUP (STABLE)
# --------------------------------------------------
model = None
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")
    st.write("Gemini API loaded:", bool(api_key))
except Exception as e:
    st.warning(f"Gemini disabled: {e}")

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(
        """
        <h1>Hey, I'm <span style="color:#6a11cb;">Ganesh Sarode 👋</span></h1>
        <h3>BTech Student | Engineering Aspirant</h3>
        <p>Focused on DSA, Python, and real-world problem solving.</p>
        """,
        unsafe_allow_html=True,
    )

with col2:
    if lottie_person:
        st_lottie(lottie_person, height=300)

st.divider()

# --------------------------------------------------
# CHATBOT SECTION
# --------------------------------------------------
st.subheader("💬 Ask Me Anything About Ganesh")

question = st.text_input("Type your question")

if question:
    if model:
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(
                    f"You are an assistant for Ganesh Sarode.\n\nUser: {question}"
                )
                st.success(response.text)
            except Exception as e:
                st.error(f"AI error: {e}")
    else:
        st.error("Gemini model not available")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()
st.write("✨ Built with Python & Streamlit")
