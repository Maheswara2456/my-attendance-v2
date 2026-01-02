import streamlit as st

def manual_edit(df):
    st.subheader("✏️ Manual Edit")

    edited_df = st.data_editor(df, use_container_width=True)

    if st.button("💾 Save Manual Changes"):
        return edited_df, True

    return df, False
