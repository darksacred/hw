import re

with open('mfile_5_6.txt', 'r', encoding='utf-8') as file:
    dic = {}
    for line in file:
        num = []
        key, *value = line.split(' ' and ':')
        for el in value:
            num += (re.findall(r'\d+', el))
        num = [int(x) for x in num]
        num_r = sum(num)
        dic[key] = num_r
print(dic)
