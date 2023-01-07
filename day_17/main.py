from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text=question['text']
    question_answer=question['answer']
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

take_quiz = QuizBrain(question_bank)

while take_quiz.still_has_questions():
    take_quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {take_quiz.score}/{take_quiz.question_number}")