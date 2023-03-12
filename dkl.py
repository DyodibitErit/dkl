import os

code = []
string = 0
file = open("config", "r")

for line in file:
    code.append(line)
    if "title:" in code[string]:
        os.system("title " + line[6:])
    elif "main:" in code[string]:
        main = line[5:]
    elif "start" in code[string]:
        os.system("starter " + main)
    string += 1