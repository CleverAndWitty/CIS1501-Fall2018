file_name = input("Enter a file to write: ")
content = ""

try:
    some_file = open(file_name, 'w')

    content = ""

    while content != 'DONE':
        content = input("Enter something to write to the file or DONE")
        if content != "DONE":
            some_file.write(content)
            some_file.write("\n")

finally:
    some_file.close()
