import streamlit as st

from utils.data_loader import load_data, save_data
from ui.styles import apply_styles
from ui.cards import render_cards
from features.export_data import export_data

from features.daily_entry import daily_entry
from features.manual_edit import manual_edit
from features.delete_entry import delete_entry

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(page_title="My Attendance", layout="wide")
apply_styles()

st.title("📊 My Personal Attendance Dashboard")

# ===============================
# SUBJECT CONFIG
# ===============================
subjects = {
    "CD": "CD",
    "CC": "CC",
    "CSE": "CSE",
    "ANN": "ANN",
    "BCCS": "BSCE"
}

# ===============================
# LOAD DATA (always fresh)
# ===============================
df = load_data()

# ===============================
# DAILY ENTRY (ADD / REPLACE)
# ===============================
daily_entry(df, subjects)
st.divider()

# ===============================
# DELETE ENTRY (SAFE)
# ===============================
df, deleted = delete_entry(df)
if deleted:
    save_data(df)
    st.rerun()

st.divider()

# ===============================
# DASHBOARD CARDS
# ===============================
st.subheader("📘 Subject-wise Attendance")
render_cards(df, subjects)
st.divider()
st.divider()
export_data(df)
st.divider()

# ===============================
# MANUAL EDIT
# ===============================
df, changed = manual_edit(df)
if changed:
    save_data(df)
    st.success("✅ Manual changes saved")
    st.rerun()

# ===============================
# FINAL SAVE (SAFETY)
# ===============================
save_data(df)
