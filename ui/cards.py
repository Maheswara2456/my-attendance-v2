import streamlit as st
from logic.attendance_calc import (
    calculate_attendance,
    required_classes_for_75,
    predict_attendance
)

def render_cards(df, subjects):
    cols = st.columns(len(subjects))

    for i, (label, col) in enumerate(subjects.items()):
        p, t, pct = calculate_attendance(df[col])

        if t == 0:
            bg = "#2c2c2c"
            status = "No Classes"
            color = "#ccc"
            extra_html = ""
        else:
            need = required_classes_for_75(p, t)
            attend_next = predict_attendance(p, t, attend=True)
            skip_next = predict_attendance(p, t, attend=False)

            if pct < 75:
                bg = "#7f1d1d"
                status = "⚠ Low Attendance"
                color = "#facc15"
            else:
                bg = "#166534"
                status = "✅ Safe"
                color = "#4cff88"

            extra_html = (
                "<hr style='opacity:0.25'>"
                "<div style='font-size:13px;line-height:1.6'>"
                f"🎯 Need <b>{need}</b> more classes for 75%<br>"
                f"➕ Attend next: <b>{attend_next:.1f}%</b><br>"
                f"➖ Skip next: <b>{skip_next:.1f}%</b>"
                "</div>"
            )

        card_html = (
            "<div style='"
            f"background:{bg};"
            "padding:20px;"
            "border-radius:16px;"
            "text-align:center;"
            "box-shadow:0 10px 25px rgba(0,0,0,0.35);"
            "'>"
            f"<h3>{label}</h3>"
            f"<p>{p} / {t}</p>"
            f"<h2 style='color:{color}'>{pct:.1f}%</h2>"
            f"<p>{status}</p>"
            f"{extra_html}"
            "</div>"
        )

        with cols[i]:
            st.markdown(card_html, unsafe_allow_html=True)
