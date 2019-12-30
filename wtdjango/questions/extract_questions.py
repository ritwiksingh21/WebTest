from .models import Questions, MC_Answer
from uploads.models import Document
from bs4 import BeautifulSoup

def convertToObject(soup):
    questions_blocks = soup.find_all("ol", type=1) #find all ols with numbers
    for block in questions_blocks:
        questions = block.find_all("li", recursive=False)
        questionIndex = 0
        ansIndex = 0
        for question in questions:
            qobject = Question.objects.create_question()
            qobject.text = question.find_all("p", recursive=False)
            qobject.save()
            if isMultiLayered(question):
                ansIndex = 0
                for ol in question.find_all("ol"):
                    lists = ol.find_all("li")
                    for l in lists:
                        if isMultipleChoice(question):
                            mca = MC_Answer.objects.create_mc_answer(l, 'a') #add new MC_Answer object to mc_answers
                                                                             #TODO: Add letter extraction#
                            mca.save()
                            qobject.mc_answers.add(mca)
                        else:
                            l.append(soup.new_tag("br"))
                            l.append(soup.new_tag("textarea"))
                            qobject.text.append(l)
                        ansIndex += 1
            qobject.save()
