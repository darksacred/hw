import re

with open('mfile_5_5.txt', 'w') as file:
    content = input('Введите числа для суммирования: ')
    file.write(content)

with open('mfile_5_5.txt', 'r') as file:
    for el in file:
        num = el.split()
    num = [int(x) for x in num]
print(sum(num))

