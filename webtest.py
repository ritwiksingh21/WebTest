import subprocess
from bs4 import BeautifulSoup

subprocess.call(["pandoc", "-o", "output.html", "test.docx"], shell=True) #convert text to markup in output.html

with open("output.html") as fp:
    soup = BeautifulSoup(fp)

def convertToForm(soup):
    questions_blocks = soup.find_all("ol", type=1) #find all ols with numbers
    for block in questions_blocks:
        questions = block.find_all("li")
        loop = 0

        for question in questions:
            print(question)
            if isMultipleChoice(question):
                print("Multiple choice!")
                for ol in question.find_all("ol"):
                    lists = ol.find_all("li")
                    for l in lists:
                        new_input = soup.new_tag("input", type="radio")
                        l.insert_before(new_input)
                loop += 1
                print(loop)
            else:
                new_field = soup.new_tag("textarea")
                question.p.append(new_field)
                loop += 1

    f = open("output.html", "w+")
    f.write('')
    f.write(block.prettify())

def isMultipleChoice(question):
    for content in question.contents:
        if(content.name=='ol' and not "!NOTMC" in question.prettify()):
            return True
    return False

convertToForm(soup)
