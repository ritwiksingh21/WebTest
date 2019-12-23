class Question():
    def __init__(self):
        self.text = ""
        self.tags = []


class QuestionMC(Question):
    def __init__(self):
        super().__init__()
        self.answers = []
        self.correctAnswers = []
        self.correctAnswerLabels = [] #should i use this?

class Answer():
    def __init__(self, q, correct=False):
        self.question = q
        self.question.answers.append(self)
        if correct:
            self.question.correctAnswers.append(self)

class Tag():
    def __init__(self, name):
        self.name = name
