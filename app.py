import streamlit as st
import pandas as pd

from ui.styles import apply_styles
from ui.cards import render_cards
from features.export_data import export_data
from features.daily_entry import daily_entry
from features.manual_edit import manual_edit
from features.delete_entry import delete_entry
from utils.firebase_attendance import load_attendance, save_attendance


# ===============================
# PAGE CONFIG (MUST BE FIRST)
# ===============================
st.set_page_config(
    page_title="My Attendance",
    page_icon="assets/icon-512.png",
    layout="wide"
)

st.write("DEPLOY CHECK — VERSION 2026-01-04 🔥")
apply_styles()

st.title("📊 My Personal Attendance Dashboard")


# ===============================
# LOGIN
# ===============================
st.sidebar.image("assets/icon-512.png", width=110)
st.sidebar.title("🔐 Login")

user_email = st.sidebar.text_input("Enter your email")

if not user_email:
    st.warning("Please enter your email to continue")
    st.stop()

user_id = user_email.replace(".", "_").lower()


# ===============================
# SUBJECT CONFIG
# ===============================
subjects = {
    "CD": "CD",
    "CC": "CC",
    "CSE": "CSE",
    "ANN": "ANN",
    "BCCS": "BCCS"
}


# ===============================
# LOAD DATA (ONCE)
# ===============================
if "df" not in st.session_state:
    raw_data = load_attendance(user_id)
    st.session_state.df = (
        pd.DataFrame(raw_data)
        if raw_data
        else pd.DataFrame(columns=["DATE", *subjects.keys()])
    )

df = st.session_state.df


# ===============================
# DAILY ENTRY
# ===============================
updated = daily_entry(df, subjects)
if updated:
    save_attendance(user_id, df.to_dict(orient="records"))
    st.session_state.df = df
    st.rerun()

st.divider()


# ===============================
# DELETE ENTRY
# ===============================
df, deleted = delete_entry(df)
if deleted:
    save_attendance(user_id, df.to_dict(orient="records"))
    st.session_state.df = df
    st.rerun()

st.divider()


# ===============================
# DASHBOARD
# ===============================
st.subheader("📘 Subject-wise Attendance")
render_cards(df, subjects)

st.divider()


# ===============================
# EXPORT
# ===============================
export_data(df)

st.divider()


# ===============================
# MANUAL EDIT
# ===============================
df, changed = manual_edit(df)
if changed:
    save_attendance(user_id, df.to_dict(orient="records"))
    st.session_state.df = df
    st.success("✅ Manual changes saved")
    st.rerun()
