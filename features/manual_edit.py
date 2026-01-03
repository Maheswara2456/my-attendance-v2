import streamlit as st


def manual_edit(df):
    st.subheader("✏️ Manual Edit (Advanced)")

    # Safety: no data
    if df.empty:
        st.info("No attendance data available to edit")
        return df, False

    edited_df = st.data_editor(
        df,
        use_container_width=True,
        num_rows="dynamic"
    )

    if st.button("💾 Save Manual Changes"):
        if edited_df.equals(df):
            st.info("No changes detected")
            return df, False

        return edited_df, True

    return df, False
