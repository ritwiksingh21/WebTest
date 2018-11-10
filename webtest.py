import subprocess
from bs4 import BeautifulSoup

subprocess.call(["pandoc", "-o", "output.html", "test.docx"], shell=True) #convert text to markup in output.html

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

with open("output.html") as fp:
    soup = BeautifulSoup(fp)

def convertToForm(soup):
    questions_blocks = soup.find_all("ol", type=1) #find all ols with numbers
    returnString = ""
    #print(soup.find_all("li"), recursive=False)
    for block in questions_blocks:
        questions = block.find_all("li", recursive=False)
        questionIndex = 0
        ansIndex = 0
        for question in questions:
            if isMultiLayered(question):
                ansIndex = 0
                for ol in question.find_all("ol"):
                    lists = ol.find_all("li")
                    for l in lists:
                        if isMultipleChoice(question):
                            new_input = soup.new_tag("input", type="radio")
                            new_input['name'] = questionIndex
                            new_input['value'] = letters[ansIndex]
                            l.p.string.insert_before(new_input)
                        else:
                            l.append(soup.new_tag("br"))
                            l.append(soup.new_tag("textarea"))
                        ansIndex += 1
            else:
                question.p.append(soup.new_tag("br"))
                question.p.append(soup.new_tag("textarea"))
            questionIndex += 1
        setAllStarts(block)
        returnString += block.prettify()

    return returnString


def isMultipleChoice(question):
    for content in question.contents:
        if(content.name=='ol' and not "!NOTMC" in question.prettify()):
            return True
    return False

def isMultiLayered(question):
    for content in question.contents:
        if(content.name=='ol'):
            return True
    return False

def setAllStarts(soup):
    ols = soup.find_all("ol")
    for l in ols:
        l['start'] = 1


f = open("output2.html", "w", encoding='utf8')
f.write('')
f.write(convertToForm(soup))
f.close()
f = open("output2.html", "r")
contents = ""
for line in f:
    contents += line

contents = "<html><body><form>" + contents + "</form></body></html>"
contents.replace("!NOTMC", "")
f.close()

f = open("output2.html", "w", encoding='utf8')
f.write(contents)
f.close()
