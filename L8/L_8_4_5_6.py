class Orgtechnika:
    def __init__(self, name, cena, kolvo, number_of_lists, *args):
        self.name = name
        self.cena = cena
        self.kolvo = kolvo
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.cena, 'Количество': self.kolvo}

    def __str__(self):
        return f'{self.name} цена {self.cena} количество {self.kolvo}'

    def reception(self):
        try:
            a = input(f'Введите наименование ')
            b = int(input(f'Введите цену за ед '))
            c = int(input(f'Введите количество '))
            poz = {'Модель устройства': a, 'Цена за ед': b, 'Количество': c}
            self.my_unit.update(poz)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Orgtechnika.reception(self)


class Printer(Orgtechnika):
    def to_print(self):
        return f'Номер в листе {self.numb} '


class Copier(Orgtechnika):
    def to_copier(self):
        return f'Номер в листе {self.numb} '


class Scanner(Orgtechnika):
    def to_scan(self):
        return f'Номер в листе {self.numb} '


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 15)
unit_3 = Copier('Xerox', 1500, 1, 20)
print(unit_3.to_copier())
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copier())

#        self._income = {"Wage": wage, "Bonus": bonus}
#    def __init__(self, name, surname, position, wage, bonus):
#        super().__init__(name, surname, position, wage, bonus)
