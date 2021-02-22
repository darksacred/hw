ls = {'One': 'Один ', 'Two': 'Два ', 'Three': 'Три ', 'Four': 'Четыре '}
new_file = []
with open('mfile_5_4.txt', 'r', encoding='utf-8') as file:
    for i in file:
        i = i.split(' ', 1,)
        new_file.append(ls[i[0]] + i[1])

with open('mfile_5_4_new.txt', 'w', encoding='utf-8') as file_2:
    file_2.writelines(new_file)

file_2 = open('mfile_5_4_new.txt', 'r', encoding='utf-8')
print(file_2.read())
file_2.close()