from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
score = 0
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
while(quiz.havequestions()):
    if quiz.next_question() == True:
        print("Correct.")
        score += 1
        print(f"Score: {score}")
    else:
        print("Wrong.")
        print(f"Score: {score}")
print(f"Final Score: {score}/{len(question_bank)}")
