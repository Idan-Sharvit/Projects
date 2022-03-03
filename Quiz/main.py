from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question['question'], question['correct_answer']))


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()


percentage = quiz.score/len(quiz.question_list) * 100
print(f"You have completed the quiz with {round(percentage, 2)}% success")