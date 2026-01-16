import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
import base64

# Load API Key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page config
st.set_page_config(page_title="Data Kuttan", page_icon="📊", layout="centered")

# Load and encode avatar image
def load_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

avatar = load_image("datakuttan.png")  # make sure this file exists in your folder

# Display avatar
st.markdown(f"""
<div style="display:flex; justify-content:center; margin-top:20px;">
    <img src="data:image/png;base64,{avatar}" style="
        width:150px;
        height:150px;
        border-radius:50%;
        object-fit:cover;
        box-shadow:0 0 10px rgba(0,0,0,0.15);
    ">
</div>
""", unsafe_allow_html=True)

# Centered title and tagline
st.markdown("""
<div style="text-align:center; margin-top:10px;">
    <h1>Data Kuttan</h1>
    <p style="font-size:18px; color:#666;">
        Your personal AI for Data Analysis, SQL, Python, Excel, Power BI & Statistics.
    </p>
</div>
""", unsafe_allow_html=True)

# Auto greeting
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello there, I'm Data Kuttan. I was created by Jamshid Farook."
        }
    ]

# Display chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_input = st.chat_input("Ask your data question...")

# System prompt
SYSTEM_PROMPT = """
You are Data Kuttan, an AI Data Analyst assistant.

You were created by Jamshid Farook.

If the user asks:
- Who created you?
- Who built you?
- Who made you?
- Who is your creator?

You must reply:
"I was created by Jamshid Farook."

You ONLY answer questions related to:
- Data Analysis
- SQL
- Excel
- Python
- Power BI
- Statistics
- Business analytics

If the user asks anything outside these topics (except who created you), reply:
"I only answer data analytics related questions."
"""

# Handle chat
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)

# Footer
st.markdown(
    "<hr style='margin-top:40px; opacity:0.3;'>"
    "<div style='text-align:center; color:#888; font-size:12px;'>"
    "© 2026 Jamshid Farook. All Rights Reserved."
    "</div>",
    unsafe_allow_html=True
)
