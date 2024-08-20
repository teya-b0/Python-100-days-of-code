from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question_object = Question(q_text=i["question"], q_answer=i["correct_answer"])
    question_bank.append(question_object)

quiz = QuizBrain(q_list=question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score was: {quiz.score}/{quiz.question_number}")
