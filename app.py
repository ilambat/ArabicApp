import streamlit as st
import random

st.set_page_config(page_title="Arabic Vocabulary Quiz")

# Updated Vocabulary list
vocab = [
    {"arabic": "كِتَابٌ", "english": "Book"},
    {"arabic": "قَلَمٌ", "english": "Pen"},
    {"arabic": "مِسْطَرَةٌ", "english": "Ruler"},
    {"arabic": "مِمْحَاةٌ", "english": "Eraser"},
    {"arabic": "دَفْتَرٌ", "english": "Notebook"},
    {"arabic": "مَكْتَبٌ", "english": "Desk"},
    {"arabic": "طَاوِلَةٌ", "english": "Table"},
    {"arabic": "سَبُّورَةٌ", "english": "Blackboard"},
    {"arabic": "كُرْسِيٌّ", "english": "Chair"},
    {"arabic": "شَنْطَةٌ", "english": "Bag"},
    {"arabic": "سَيَّارَةٌ", "english": "Car"},
    {"arabic": "بَابٌ", "english": "Door"},
    {"arabic": "نَافِذَةٌ", "english": "Window"},
    {"arabic": "كُرَةٌ", "english": "Ball"},
    {"arabic": "دَبَّاسَةٌ", "english": "Stapler"},
    {"arabic": "هَاتِفٌ", "english": "Telephone"},
    {"arabic": "خِزَانَةٌ", "english": "Cupboard"},
    {"arabic": "غَسَّالَةٌ", "english": "Washing machine"},
    {"arabic": "قِفْلٌ", "english": "Lock"},
    {"arabic": "مِذْيَاعٌ", "english": "Radio"},
    {"arabic": "شَمْعَةٌ", "english": "Candle"}
]

st.title("📝 Arabic Vocabulary Quiz")
quiz_type = st.radio("Choose quiz direction:", ["Arabic → English", "English → Arabic"], horizontal=True)

# Load or reset session state
if "question" not in st.session_state or st.button("Next Question"):
    question = random.choice(vocab)
    options = random.sample([v for v in vocab if v != question], 3) + [question]
    random.shuffle(options)
    st.session_state.question = question
    st.session_state.options = options
    st.session_state.answered = False
    st.session_state.feedback = ""

question = st.session_state.question
options = st.session_state.options

# Display question and collect answer
if quiz_type == "Arabic → English":
    st.markdown(f"### What is the meaning of: **{question['arabic']}**?")
    choices = [opt["english"] for opt in options]
    selected = st.radio("Select your answer:", [""] + choices, index=0, key="quiz_ae")

    if selected and not st.session_state.answered:
        if selected == question["english"]:
            st.session_state.feedback = "✅ Correct!"
        else:
            st.session_state.feedback = f"❌ Incorrect. The correct answer is: **{question['english']}**"
        st.session_state.answered = True

elif quiz_type == "English → Arabic":
    st.markdown(f"### What is the Arabic for: **{question['english']}**?")
    choices = [opt["arabic"] for opt in options]
    selected = st.radio("Select your answer:", [""] + choices, index=0, key="quiz_ea")

    if selected and not st.session_state.answered:
        if selected == question["arabic"]:
            st.session_state.feedback = "✅ Correct!"
        else:
            st.session_state.feedback = f"❌ Incorrect. The correct answer is: **{question['arabic']}**"
        st.session_state.answered = True

# Show feedback if available
if st.session_state.feedback:
    st.info(st.session_state.feedback)
