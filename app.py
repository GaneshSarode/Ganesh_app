import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Ganesh Sarode | Portfolio",
    page_icon="💻",
    layout="wide"
)

# --------------------------------------------------
# THEME STATE
# --------------------------------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

dark_mode = st.toggle("🌙 Dark Mode", st.session_state.theme == "dark")
st.session_state.theme = "dark" if dark_mode else "light"

# --------------------------------------------------
# STYLES (DARK + 3D)
# --------------------------------------------------
if st.session_state.theme == "dark":
    bg = "#0e1117"
    text = "#e6e6e6"
    card = "#161b22"
else:
    bg = "#ffffff"
    text = "#000000"
    card = "#f4f4f4"

st.markdown(f"""
<style>
.stApp {{
    background-color: {bg};
    color: {text};
}}

.card {{
    background: {card};
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    margin-bottom: 22px;
}}

.card:hover {{
    transform: translateY(-6px);
    box-shadow: 0 18px 40px rgba(0,0,0,0.25);
}}

a {{
    text-decoration: none;
    font-weight: 600;
}}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HERO
# --------------------------------------------------
st.title("Ganesh Sarode")
st.subheader("BTech | EXTC | VJTI Mumbai")

st.write(
    "Focused on **Data Structures, Python, and building deployable applications**. "
    "Interested in software engineering and problem-solving driven roles."
)

st.divider()

# --------------------------------------------------
# RESUME
# --------------------------------------------------
st.header("📄 Resume")

with open("resume.pdf", "rb") as file:
    st.download_button(
        label="⬇️ Download Resume (PDF)",
        data=file,
        file_name="Ganesh_Sarode_Resume.pdf",
        mime="application/pdf"
    )


# --------------------------------------------------
# SKILLS
# --------------------------------------------------
st.header("🛠 Skills")

st.markdown("""
<div class="card">
<b>Programming:</b> Python, Basic C / C++ <br><br>
<b>Core CS:</b> Data Structures & Algorithms, Problem Solving <br><br>
<b>Tools:</b> Streamlit, Git & GitHub, Basic Machine Learning
</div>
""", unsafe_allow_html=True)

st.divider()

# --------------------------------------------------
# PROJECTS (WITH GITHUB LINKS)
# --------------------------------------------------
st.header("📌 Projects")

st.markdown("""
<div class="card">
<h4>🤖 JARVIS – Voice Assistant</h4>
<b>Problem:</b> Manual interaction is inefficient for repetitive tasks.<br>
<b>Solution:</b> Python-based voice assistant executing commands using speech recognition.<br>
<b>Tech:</b> Python, Speech Recognition, Text-to-Speech.<br>
<b>Learning:</b> API integration, real-time input handling, debugging.<br><br>
🔗 <a href="https://github.com/GaneshSarode/jarvis-ai-voice-assistant-" target="_blank">View on GitHub</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h4>🔐 Digital Lock System</h4>
<b>Problem:</b> Traditional lock systems lack flexibility and customization.<br>
<b>Solution:</b> Logic-based digital lock with authentication control.<br>
<b>Tech:</b> Digital Logic, Embedded Systems concepts.<br>
<b>Learning:</b> Logical design, hardware–software interaction.<br><br>
🔗 <a href="https://github.com/GaneshSarode/Digital-Logic-Keypad-Lock" target="_blank">View on GitHub</a>
</div>
""", unsafe_allow_html=True)

st.divider()

# --------------------------------------------------
# CERTIFICATIONS (CLICKABLE)
# --------------------------------------------------
st.header("📜 Certifications")

st.markdown("""
# <div class="card">
# <h4>🎓 Python for Everybody</h4>
# <b>Platform:</b> Coursera<br>
# 🔗 <a href="PASTE_COURSERA_LINK_HERE" target="_blank">View Certificate</a>
# </div>

<div class="card">
<h4>🎓 Data Science s</h4>
<b>Platform:</b> Coursera<br>
🔗 <a href="PASTE_COURSERA_LINK_HERE" target="_blank">View Certificate</a>
</div>

<div class="card">
<h4>🎓 Machine Learning </h4>
<b>Platform:</b> Coursera<br>
🔗 <a href="PASTE_COURSERA_LINK_HERE" target="_blank">View Certificate</a>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LINKS
# --------------------------------------------------
st.header("🔗 Links")

st.markdown("""
<div class="card">
<b>GitHub:</b>"https://github.com/GaneshSarode" <br>
<b>LinkedIn:</b> www.linkedin.com/in/ganesh-sarode-1bb40136a <br>
<b>Email:</b> ganeshsarode3015@gmail.com
</div>
""", unsafe_allow_html=True)

st.divider()
st.write("📍 Built with Python & Streamlit")
