f = open("output2.html", "r")
contents = ""
for line in f.readlines():
    contents += line
print(contents)
print("Hello")
