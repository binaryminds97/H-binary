"""
Phase 1 skeleton for JeevanMitra AI
Entry point (Streamlit). Minimal UI: landing page and language selector.
Do not call any AI or external services in Phase 1.
"""

import streamlit as st

st.set_page_config(page_title="JeevanMitra AI (Phase 1)", layout='centered')

if 'language' not in st.session_state:
    st.session_state.language = 'English'

st.title("JeevanMitra AI")
st.markdown("""
**Voice-first Livelihood & Skilling Assistant (Prototype)**

This is Phase 1: project skeleton. Approve the plan to proceed to the next phase.
""")

with st.sidebar:
    st.header("Language")
    lang = st.radio("Choose language", options=["English", "Hindi", "Marathi"], index=0)
    st.session_state.language = lang
    st.write(f"Selected: {st.session_state.language}")

st.write("\n")

col1, col2 = st.columns([3,1])
with col1:
    st.header("Your voice. Your skills. Your livelihood.")
    st.write("A multilingual AI assistant that helps beneficiaries discover suitable NSQF-aligned training and livelihood pathways.")
    st.write("")
    if st.button("Start My Livelihood Journey"):
        st.info("(Phase 1) The interview UI will be implemented in Phase 3. For now this is a placeholder.")
with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/8/87/Big_blue_circle.png", width=120)

st.markdown("---")
st.subheader("Phase 1: Project skeleton created")
st.write("Folders: pages/, components/, services/, database/, data/, prompts/, utils/, tests/")

st.caption("Do not commit secrets. Use .env or Streamlit secrets for credentials.")
