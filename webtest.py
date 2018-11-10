import subprocess
from bs4 import BeautifulSoup

subprocess.call(["pandoc", "-o", "output.html", "test.docx"], shell=True) #convert text to markup in output.html

with open("output.html") as fp:
    soup = BeautifulSoup(fp)

def convertToForm(soup):
    questions_blocks = soup.find_all("ol", type=1) #find all ols with numbers
    for block in questions_blocks:
        questions = block.find_all("li")
        for question in questions:
            new_field = soup.new_tag("textarea")
            question.p.append(new_field)
    print(questions)
    f = open("output.html", "w+")
    f.write('')
    f.write(block.prettify())

convertToForm(soup)
