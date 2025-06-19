
import streamlit as st
import random

st.set_page_config(page_title="Arabic Vocabulary Quiz")

# Vocabulary list
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
    {"arabic": "سَيَّارَةٌ", "english": "Car"},
    {"arabic": "بَابٌ", "english": "Door"},
    {"arabic": "نَافِذَةٌ", "english": "Window"},
    {"arabic": "كُرَةٌ", "english": "Ball"},
]

st.title("📝 Arabic Vocabulary Quiz")
quiz_type = st.radio("Choose quiz direction:", ["Arabic → English", "English → Arabic"])

# Shuffle and pick one question
question = random.choice(vocab)
options = random.sample(vocab, 3) + [question]
random.shuffle(options)

# Display the question and options
if quiz_type == "Arabic → English":
    st.markdown(f"### What is the meaning of: **{question['arabic']}**?")
    choices = [opt["english"] for opt in options]
    answer = st.radio("Choose the correct translation:", choices)
    if st.button("Check Answer"):
        if answer == question["english"]:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect. The correct answer is: **{question['english']}**")

elif quiz_type == "English → Arabic":
    st.markdown(f"### What is the Arabic for: **{question['english']}**?")
    choices = [opt["arabic"] for opt in options]
    answer = st.radio("Choose the correct Arabic word:", choices)
    if st.button("Check Answer"):
        if answer == question["arabic"]:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect. The correct answer is: **{question['arabic']}**")
