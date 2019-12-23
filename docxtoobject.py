import subprocess
import json, os
from bs4 import BeautifulSoup
from qclass import Question, QuestionMC
from docxtowebform import isMultiLayered, isMultipleChoice

subprocess.call(["pandoc", "-o", "output.json", "output2.html"], shell=True) #convert text to markup in output.html

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']


with open("output.html") as fp:
    soup = BeautifulSoup(fp)

def convertToObject(soup):
    questions_blocks = soup.find_all("ol", type=1) #find all ols with numbers
    for block in questions_blocks:
        questions = block.find_all("li", recursive=False)
        questionIndex = 0
        ansIndex = 0
        for question in questions:
            qobject = QuestionMC()
            qobject.text = question.find_all("p", recursive=False)
            print(qobject.text)
            if isMultiLayered(question):
                ansIndex = 0
                for ol in question.find_all("ol"):
                    lists = ol.find_all("li")
                    for l in lists:
                        if isMultipleChoice(question):
                            qobject.answers.append(l)
                            print(qobject.answers)
                        else:
                            l.append(soup.new_tag("br"))
                            l.append(soup.new_tag("textarea"))
                        ansIndex += 1

convertToObject(soup)
