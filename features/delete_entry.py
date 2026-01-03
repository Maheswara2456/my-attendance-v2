import streamlit as st


def delete_entry(df):
    st.subheader("🗑️ Delete Entire Date (Safe)")

    # Safety: no data
    if df.empty or "DATE" not in df.columns:
        st.info("No attendance data available")
        return df, False

    date_to_delete = st.selectbox(
        "Select date to delete",
        [""] + df["DATE"].tolist()
    )

    if date_to_delete:
        st.warning("⚠️ You are about to delete this record:")
        st.dataframe(
            df[df["DATE"] == date_to_delete],
            use_container_width=True
        )

        confirm = st.checkbox("I understand this cannot be undone")

        if confirm:
            if st.button("❌ Confirm Delete"):
                df = df[df["DATE"] != date_to_delete]
                st.success("✅ Date deleted successfully")
                return df, True
        else:
            st.info("Please confirm before deleting")

    return df, False
