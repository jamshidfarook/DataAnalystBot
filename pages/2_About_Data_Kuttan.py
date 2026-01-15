import streamlit as st
import base64

st.set_page_config(page_title="About Data Kuttan", layout="centered")

def load_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

avatar = load_image("datakuttan.png")

st.markdown(f"""
<div style="text-align:center; margin-top:30px;">
    <img src="data:image/png;base64,{avatar}" style="
        width:160px;
        height:160px;
        border-radius:50%;
        object-fit:cover;
        box-shadow:0 0 10px rgba(0,0,0,0.15);
    ">
    <h2 style="margin-top:15px;">Data Kuttan</h2>
    <h4 style="color:#666;">AI Data Analyst Assistant</h4>
    <div style="max-width:600px; margin:auto; font-size:16px; margin-top:10px; text-align:left; line-height:1.5;">
        Data Kuttan is an AI-powered Data Analyst assistant designed to help users
        with SQL, Python, Excel, Power BI, Statistics, and business analytics.
        It was created to make data understanding easier, faster, and more practical
        for students, analysts, and professionals.
    </div>
</div>

<hr style="margin-top:40px; opacity:0.3;">

<div style="text-align:center; color:#888; font-size:13px; margin-top:10px;">
    Always remember that AI also makes mistakes.
</div>
""", unsafe_allow_html=True)
