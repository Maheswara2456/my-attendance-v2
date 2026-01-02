import streamlit as st
from datetime import date

def daily_entry(df, subjects):
    st.subheader("📝 Daily Attendance Entry")

    # ✅ Ensure DATE column exists
    if "DATE" not in df.columns:
        df.insert(0, "DATE", "")

    entry_date = st.date_input(
        "Select Date",
        date.today()
    ).strftime("%d-%m-%Y")

    mode = st.radio(
        "Action",
        ["ADD", "REPLACE"],
        horizontal=True
    )

    attendance_options = ["", "P", "A", "P-P", "A-A", "P-LAB", "A-LAB"]
    input_data = {}

    cols = st.columns(len(subjects))
    for i, (label, col) in enumerate(subjects.items()):
        with cols[i]:
            input_data[col] = st.selectbox(
                label,
                attendance_options,
                key=f"{col}_{entry_date}"
            )

    if st.button("💾 Save Attendance"):
        if entry_date in df["DATE"].values:
            idx = df.index[df["DATE"] == entry_date][0]

            for col, val in input_data.items():
                if not val:
                    continue

                old_val = df.at[idx, col]

                if mode == "ADD" and old_val:
                    df.at[idx, col] = f"{old_val}+{val}"
                else:
                    df.at[idx, col] = val
        else:
            new_row = {"DATE": entry_date}
            for col in subjects.values():
                new_row[col] = input_data.get(col, "")
            df.loc[len(df)] = new_row

        st.success("✅ Attendance saved")
        st.rerun()
