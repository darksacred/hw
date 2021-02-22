file = open('mfile_5_2.txt', 'r', encoding='utf-8')
kol_strok = 0
for el in file:
    kol_slov = len(el.split())
    print(f'Количество слов в строке: {kol_slov} \n', end='')
    kol_strok += 1
print(f'Количество строк: {kol_strok}')
file.close()
