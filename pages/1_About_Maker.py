import streamlit as st
import base64

st.set_page_config(page_title="About the Maker", layout="centered")

def load_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

photo = load_image("jamshid.png")

st.markdown(f"""
<div style="text-align:center; margin-top:30px;">
    <img src="data:image/png;base64,{photo}" style="
        width:160px;
        height:160px;
        border-radius:50%;
        object-fit:cover;
        box-shadow:0 0 10px rgba(0,0,0,0.15);
    ">
    <h2 style="margin-top:15px;">Jamshid Farook</h2>
    <h4 style="color:#666;">Data Analyst</h4>
    <div style="max-width:600px; margin:auto; font-size:16px; margin-top:10px; text-align:left; line-height:1.5;">
        Detail-oriented Data Analyst with hands-on experience in Python, SQL, Excel, 
        and data visualization tools. IBM Data Analyst Certified with proven experience 
        in dashboards, real-world datasets, and actionable insights.
    </div>
    <div style="margin-top:20px;">
        🌐 <a href="https://jamshidfarook.github.io/" target="_blank">
            https://jamshidfarook.github.io/
        </a>
    </div>
</div>
""", unsafe_allow_html=True)
