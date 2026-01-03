import streamlit as st
from logic.attendance_calc import calculate_attendance


def render_cards(df, subjects):
    """
    Render subject-wise attendance cards
    """

    # If dataframe is empty
    if df.empty:
        st.info("No attendance data available")
        return

    cols = st.columns(len(subjects))

    for col_ui, (col_name, label) in zip(cols, subjects.items()):
        with col_ui:
            st.markdown(f"### {label}")

            # Safety: column missing
            if col_name not in df.columns:
                st.metric(
                    label="Attendance",
                    value="0.00%",
                    delta="No Classes"
                )
                continue

            # Calculate attendance
            present, total, percent = calculate_attendance(df[col_name])

            # Display card
            if total == 0:
                st.metric(
                    label="Attendance",
                    value="0.00%",
                    delta="No Classes"
                )
            else:
                st.metric(
                    label="Attendance",
                    value=f"{percent:.2f}%",
                    delta=f"{present}/{total}"
                )
