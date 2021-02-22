with open('mfile_5_3.txt', 'r', encoding='utf-8') as mfile:
    sred_oklad = []
    min_oklad = []
    my_list = mfile.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            min_oklad.append(i[0])
        sred_oklad.append(i[1])
print(f'Оклад меньше 20.000р {min_oklad}, средний оклад {sum(map(int, sred_oklad)) / len(sred_oklad)}')
mfile.close()
