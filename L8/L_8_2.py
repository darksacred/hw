class Del_null:
    def __init__(self, n_1, n_2):
        self.n_1 = n_1
        self.n_2 = n_2

    @classmethod
    def del_null(cls, n_1, n_2):
        if n_2 != 0:
            return f'{n_1 / n_2}'
        elif n_2 == 0:
            return f'Вы ввели делитель "0", число остаётся прежним {n_1}'


del_number = Del_null(2, 3)
print(del_number.del_null(2, 0))
