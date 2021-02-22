file = open("../my_file.txt", 'w')
while True:
    content = input("Введите строку: ")
    file.writelines(content + '\n')
    if not content:
        break
file.close()

files = open("../my_file.txt", 'r')
print(files.read())
