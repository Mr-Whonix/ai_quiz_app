import quiz_app as qa
import streamlit as sl

sl.title("AI Quiz Application")
sl.write("Enter your favorite quiz topic and choose the number of questions.")


userTopic = sl.text_input("Enter your topic:")
numQuestions = 0
numUniqueKey = "number of questions key"

while numQuestions <= 0:
   numQuestions = int(sl.number_input("Enter then number of questions:", min_value= 1, step = 1, key = numUniqueKey))
   if numQuestions >= 0:
      break
   
start_quiz_key = "start_quiz_key"
startQuiz = sl.button("Start Quiz", key = start_quiz_key)

if startQuiz:
    results = qa.quiz_Questions(userTopic, numQuestions)
    sl.text(results['qtionsNumbers'])

finish_quiz_key = "finish_quiz_key"
finishQuiz = sl.button("Finish Quiz", key = finish_quiz_key)

if finishQuiz:
   sl.write("Quiz Completed.")

    


   





