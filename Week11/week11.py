import os

file_name = input("Enter a file to read: ")
content = ""

if os.path.exists(file_name):
    try:
        some_file = open(file_name)
        content = some_file.readlines()
    except Exception as e:
        print(e)
    finally:
        some_file.close()

if content:
    for line in content:
        print(line, end="")