# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
import json

file = open('mfile_5_7.txt', encoding='utf-8')
firm_prib = {}
firm_ubatok = {}
firm_sred = {}
my_list = []

for i in file:
    i = i.split(' ')
    prib = (int(i[2]) - int(i[3]))
    if prib < 0:
        firm_ubatok[i[0]] = prib
    elif prib > 0:
        firm_prib[i[0]] = prib
        firm_sred[i[0]] = round(prib / 12, 2)

my_list.append(firm_prib)
my_list.append(firm_sred)
my_list.append(firm_ubatok)

with open('../list_firm.json', 'w', encoding='utf-8') as file1:
    json.dump(my_list, file1)
with open('../list_firm.json', 'r', encoding='utf-8') as file1:
    res = json.load(file1)
    print(res)

file.close()
