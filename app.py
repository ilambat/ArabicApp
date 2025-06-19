import streamlit as st
import random

st.set_page_config(page_title="Arabic Vocabulary Quiz")

# Vocabulary list
vocab = [
    {"arabic": "كِتَابٌ", "english": "Book"},
    {"arabic": "قَلَمٌ", "english": "Pen"},
    {"arabic": "مِسْطَرَةٌ", "english": "Ruler"},
    {"arabic": "مِمْحَاةٌ", "english": "Eraser/Rubber"},
    {"arabic": "دَفْتَرٌ", "english": "Notebook"},
    {"arabic": "مَكْتَبٌ", "english": "Desk"},
    {"arabic": "طَاوِلَةٌ", "english": "Table"},
    {"arabic": "سَبُّورَةٌ", "english": "Blackboard"},
    {"arabic": "كُرْسِيٌّ", "english": "Chair"},
    {"arabic": "شَنْطَةٌ", "english": "Bag"},
    {"arabic": "بَابٌ", "english": "Door"},
    {"arabic": "كُرَةٌ", "english": "Ball"},
    {"arabic": "بَيْتٌ", "english": "House"},
    {"arabic": "هَاتِفٌ", "english": "Telephone"},
    {"arabic": "مِقَصٌّ", "english": "Scissors"},
    {"arabic": "دَبَّاسَةٌ", "english": "Stapler"},
    {"arabic": "مِبْرَاةٌ", "english": "Sharpener"},
    {"arabic": "حَاسُوبٌ", "english": "Computer"},
    {"arabic": "دُولَابٌ", "english": "Cupboard"},
    {"arabic": "غَسَّالَةٌ", "english": "Washing Machine"},
    {"arabic": "قُفْلٌ", "english": "Lock"},
    {"arabic": "مِذْيَاعٌ", "english": "Radio"},
    {"arabic": "شَمْعَةٌ", "english": "Candle"},
]

# Init session state
if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.quiz_type = "Arabic → English"
    st.session_state.questions = []
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.past_wrong_words = set()
    st.session_state.selected = None
    st.session_state.history = []

# Start new test
if not st.session_state.started or st.button("🔁 Start New Test"):
    st.session_state.quiz_type = st.radio("Choose quiz direction:", ["Arabic → English", "English → Arabic"], key="quiz_type_selector")
    st.session_state.questions = random.sample(vocab, 20)
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.selected = None
    st.session_state.started = True
    st.stop()

# End of test
if st.session_state.index >= 20:
    st.markdown("## ✅ Test Completed!")
    st.markdown(f"### Your Score: **{st.session_state.score} / 20**")
    percent = round((st.session_state.score / 20) * 100)
    st.session_state.history.append(f"{st.session_state.score}/20 ({percent}%)")

    with st.expander("📊 See detailed results"):
        for ans in st.session_state.answers:
            st.markdown(
                f"- **Q:** {ans['question']}  \n"
                f"**Your answer:** {ans['your_answer']}  \n"
                f"**Correct answer:** {ans['correct_answer']}  \n"
                f"**Result:** {ans['result']} {'⚠️ (Previously incorrect)' if ans['flagged'] else ''}"
            )

    if st.session_state.history:
        with st.expander("📈 Test History"):
            for i, entry in enumerate(st.sess
