import streamlit as st

def export_data(df):
    st.subheader("📤 Export Attendance")

    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download CSV",
        data=csv_data,
        file_name="attendance.csv",
        mime="text/csv"
    )
