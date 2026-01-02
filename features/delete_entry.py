import streamlit as st

def delete_entry(df):
    st.subheader("🗑️ Delete Entire Date (Safe)")

    if df.empty:
        st.info("No data available")
        return df, False

    date_to_delete = st.selectbox(
        "Select date to delete",
        [""] + df["DATE"].tolist()
    )

    if date_to_delete:
        st.warning("⚠️ You are about to delete this record:")
        st.dataframe(df[df["DATE"] == date_to_delete], use_container_width=True)

        confirm = st.checkbox("I understand this cannot be undone")

        if confirm and st.button("❌ Confirm Delete"):
            df = df[df["DATE"] != date_to_delete]
            st.success("✅ Date deleted successfully")
            return df, True

    return df, False
