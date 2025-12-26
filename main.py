from data import question_data
from question_model import Question

def do_question_bank():
    questions = []
    for question in question_data:
        questions.append(Question(question['text'], question['answer']))
    return questions

question_bank = do_question_bank()
print(question_bank)