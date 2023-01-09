from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#create a storage location for all the questions
question_bank = []

#put all questions into a storage locatoin
for question in question_data:
    question_text=question['question']
    question_answer=question['correct_answer']
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

#create an object to start the game
take_quiz = QuizBrain(question_bank)

#create a loop to continue playing
while take_quiz.still_has_questions():
    take_quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {take_quiz.score}/{take_quiz.question_number}")