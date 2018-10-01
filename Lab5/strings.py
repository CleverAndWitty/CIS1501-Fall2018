sentence = "I am the very model of a modern major general. something something"

fixed = ""

for index in range(len(sentence)):
    if index >= 2 \
            and fixed[index-2] == '.' \
            and fixed[index-1] == " ":
        fixed += sentence[index].upper()
    else:
        fixed += sentence[index]

print(fixed)
