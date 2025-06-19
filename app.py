# Let's fix the counter not updating and repeated questions
# We'll ensure all state values (index, selected, etc.) are correctly used and reset

fixed_app_code = """
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

# Initialization
if "history" not in st.session_state:
    st.session_state.history = []

if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.quiz_type = "Arabic → English"
    st.session_state.questions = []
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.past_wrong_words = set()
    st.session_state.selected = None
    st.session_state.feedback_shown = False

# Quiz setup
if not st.session_state.started:
    st.session_state.quiz_type = st.radio("Choose quiz direction:", ["Arabic → English", "English → Arabic"])
    if st.button("🔁 Start New Test"):
        st.session_state.questions = random.sample(vocab, 20)
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.answers = []
        st.session_state.selected = None
        st.session_state.started = True
        st.experimental_rerun()
    st.stop()

# Show results if quiz is done
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
            for i, entry in enumerate(st.session_state.history, 1):
                st.markdown(f"- Test {i}: {entry}")

    if st.button("🔁 Start New Test"):
        st.session_state.started = False
        st.experimental_rerun()
    st.stop()

# Current question
question = st.session_state.questions[st.session_state.index]
options = random.sample([v for v in vocab if v != question], 3)
options.append(question)
random.shuffle(options)

st.markdown(f"### Question {st.session_state.index + 1} of 20")

if st.session_state.quiz_type == "Arabic → English":
    st.markdown(f"**What is the meaning of:** {question['arabic']}")
    choices = [opt["english"] for opt in options]
else:
    st.markdown(f"**What is the Arabic for:** {question['english']}")
    choices = [opt["arabic"] for opt in options]

selected = st.radio("Choose one:", choices, index=None, key=f"question_{st.session_state.index}")

if selected and not st.session_state.feedback_shown:
    correct = (
        selected == question["english"]
        if st.session_state.quiz_type == "Arabic → English"
        else selected == question["arabic"]
    )
    flagged = question["english"] in st.session_state.past_wrong_words
    st.session_state.answers.append({
        "question": question["arabic"] if st.session_state.quiz_type == "Arabic → English" else question["english"],
        "correct_answer": question["english"] if st.session_state.quiz_type == "Arabic → English" else question["arabic"],
        "your_answer": selected,
        "result": "✅" if correct else "❌",
        "flagged": flagged
    })
    if correct:
        st.session_state.score += 1
    else:
        st.session_state.past_wrong_words.add(question["english"])
    st.session_state.index += 1
    st.session_state.feedback_shown = False
    st.experimental_rerun()
"""

# Save the updated and fixed version
fixed_file_path = "/mnt/data/app.py"
with open(fixed_file_path, "w", encoding="utf-8") as f:
    f.write(fixed_app_code)

fixed_file_path
