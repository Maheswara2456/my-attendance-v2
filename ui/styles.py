import streamlit as st

def apply_styles():
    st.markdown("""
    <style>
    html, body {
        font-family: 'Segoe UI', sans-serif;
    }

    .stButton button {
        background: linear-gradient(135deg, #6d28d9, #4f46e5);
        color: white;
        border-radius: 10px;
        font-weight: 600;
    }

    .stButton button:hover {
        transform: scale(1.03);
    }

    hr {
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, #333, transparent);
        margin: 25px 0;
    }
    </style>
    """, unsafe_allow_html=True)
