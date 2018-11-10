import subprocess

subprocess.call(["pandoc", "-o", "output.html", "test.docx"], shell=True) #convert text to markup in output.html
