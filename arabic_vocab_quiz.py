
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

# Initialize session state
if "test_data" not in st.session_state or st.button("Start New Test"):
    st.session_state.quiz_type = st.radio("Choose quiz direction:", ["Arabic → English", "English → Arabic"], key="quiz_type_reset")
    st.session_state.questions = random.sample(vocab, 20)
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.past_wrong_words = st.session_state.get("past_wrong_words", set())
    st.session_state.test_active = True

# Main quiz loop
if st.session_state.test_active and st.session_state.index < len(st.session_state.questions):
    question = st.session_state.questions[st.session_state.index]
    options = random.sample([v for v in vocab if v != question], 3)
    options.append(question)
    random.shuffle(options)

    if st.session_state.quiz_type == "Arabic → English":
        st.markdown(f"### {st.session_state.index + 1}/20: What is the meaning of: **{question['arabic']}**?")
        choices = [opt["english"] for opt in options]
        selected = st.radio("Choose one:", choices, index=None, key=f"q{st.session_state.index}")
        if selected:
            correct = selected == question["english"]
            st.session_state.answers.append({
                "question": question["arabic"],
                "correct_answer": question["english"],
                "your_answer": selected,
                "result": "✅" if correct else "❌",
                "flagged": question["english"] in st.session_state.past_wrong_words
            })
            if correct:
                st.session_state.score += 1
            else:
                st.session_state.past_wrong_words.add(question["english"])
            st.session_state.index += 1
            st.experimental_rerun()

    else:
        st.markdown(f"### {st.session_state.index + 1}/20: What is the Arabic for: **{question['english']}**?")
        choices = [opt["arabic"] for opt in options]
        selected = st.radio("Choose one:", choices, index=None, key=f"q{st.session_state.index}")
        if selected:
            correct = selected == question["arabic"]
            st.session_state.answers.append({
                "question": question["english"],
                "correct_answer": question["arabic"],
                "your_answer": selected,
                "result": "✅" if correct else "❌",
                "flagged": question["english"] in st.session_state.past_wrong_words
            })
            if correct:
                st.session_state.score += 1
            else:
                st.session_state.past_wrong_words.add(question["english"])
            st.session_state.index += 1
            st.experimental_rerun()

# Show result
if st.session_state.test_active and st.session_state.index >= 20:
    st.markdown("## ✅ Test Completed!")
    st.markdown(f"### Your Score: **{st.session_state.score} / 20**")

    with st.expander("📊 See detailed results"):
        for ans in st.session_state.answers:
            st.markdown(
                f"- **Q:** {ans['question']}  
"
                f"**Your answer:** {ans['your_answer']}  
"
                f"**Correct answer:** {ans['correct_answer']}  
"
                f"**Result:** {ans['result']} {'⚠️ (Previously incorrect)' if ans['flagged'] else ''}"
            )

    st.session_state.test_active = False
