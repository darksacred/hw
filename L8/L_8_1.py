class Data:
    def __init__(self, d_m_y):
        self.d_m_y = d_m_y

    @classmethod
    def classmethod(cls, d_m_y):
        ls = [int(el) for el in d_m_y.split('-')]
        return int(ls[0]), int(ls[1]), int(ls[2])

    @staticmethod
    def staticmethod(d_m_y):
        ls = [int(el) for el in d_m_y.split('-')]
        if ls[0] > 31:
            print(f'Вы ввели слишком большое первое число в дате')
        elif ls[0] < 1:
            print(f'Вы ввели недопумтимое значение')
        elif ls[1] > 12 or ls[1] < 1:
           print(f'Вы ввели не существующий месяц')
        elif ls[2] < 1:
            print(f'Вы ввели не существующий год')

    def __str__(self):
        return f'Текущая дата {Data.classmethod(self.d_m_y)}'

m1 = Data('1-11-2006')
print(m1)
m1.staticmethod('1-11-2006')
m1.staticmethod('32-11-2006')
m1.staticmethod('1-13-2006')
m1.staticmethod('1-0-2006')
m1.staticmethod('1-11-0000')

