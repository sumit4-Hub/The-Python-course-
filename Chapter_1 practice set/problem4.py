import os

directory_path = '/PC SOFTWARE'

contents = os.listdir(directory_path)

for item in contents:
    print(item)
