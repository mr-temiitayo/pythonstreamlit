import streamlit as st

if 'selected_option' not in st.session_state:
    st.session_state.selected_option = None

selected_option = st.radio("Select an option:", ['Option A', 'Option B', 'Option C'], index=None if st.session_state.selected_option is None else st.session_state.selected_option)

if selected_option is not None:
    st.session_state.selected_option = selected_option

st.write(f"You selected: {st.session_state.selected_option}")
