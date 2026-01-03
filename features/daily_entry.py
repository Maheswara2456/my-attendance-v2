import streamlit as st
from datetime import date


# -----------------------------
# Helper callbacks (NO RERUN)
# -----------------------------
def add_attendance(key, value):
    if value:
        st.session_state.attendance_buffer[key].append(value)


def remove_attendance(key):
    if st.session_state.attendance_buffer[key]:
        st.session_state.attendance_buffer[key].pop()


# -----------------------------
# Main Daily Entry UI
# -----------------------------
def daily_entry(df, subjects):
    st.subheader("📝 Daily Attendance Entry")

    # Ensure DATE column exists
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

    # -----------------------------
    # Init session buffer ONCE
    # -----------------------------
    if "attendance_buffer" not in st.session_state:
        st.session_state.attendance_buffer = {
            sub: [] for sub in subjects.keys()
        }
        st.session_state.active_date = entry_date  # ✅ FIX

    # -----------------------------
    # RESET buffer when DATE changes
    # -----------------------------
    if st.session_state.active_date != entry_date:
        for k in st.session_state.attendance_buffer:
            st.session_state.attendance_buffer[k] = []
        st.session_state.active_date = entry_date

    attendance_options = ["", "P", "A"]

    # -----------------------------
    # SUBJECT INPUT UI
    # -----------------------------
    cols = st.columns(len(subjects))

    for i, (col_name, label) in enumerate(subjects.items()):
        with cols[i]:
            st.markdown(f"**{label}**")

            # Current preview
            current = "+".join(st.session_state.attendance_buffer[col_name])
            st.caption(current if current else "—")

            choice = st.selectbox(
                "Select",
                attendance_options,
                key=f"{col_name}_select_{entry_date}"
            )

            c1, c2 = st.columns(2)

            with c1:
                st.button(
                    "➕",
                    key=f"{col_name}_add_{entry_date}",
                    use_container_width=True,
                    on_click=add_attendance,
                    args=(col_name, choice)
                )

            with c2:
                st.button(
                    "➖",
                    key=f"{col_name}_remove_{entry_date}",
                    use_container_width=True,
                    on_click=remove_attendance,
                    args=(col_name,)
                )

    # -----------------------------
    # SAVE BUTTON (ONE RERUN ONLY)
    # -----------------------------
    if st.button("💾 Save Attendance"):
        if entry_date in df["DATE"].values:
            idx = df.index[df["DATE"] == entry_date][0]
        else:
            df.loc[len(df)] = {"DATE": entry_date}
            idx = df.index[-1]

        for col_name, values in st.session_state.attendance_buffer.items():
            if not values:
                continue

            combined = "+".join(values)

            old_val = df.at[idx, col_name] if col_name in df.columns else ""

            if mode == "ADD" and isinstance(old_val, str) and old_val:
                df.at[idx, col_name] = f"{old_val}+{combined}"
            else:
                df.at[idx, col_name] = combined

        # Clear buffer AFTER save
        for k in st.session_state.attendance_buffer:
            st.session_state.attendance_buffer[k] = []

        st.success("✅ Attendance saved")
        return True  # ✅ FIX: tell app.py something changed

    return False  # ✅ FIX
