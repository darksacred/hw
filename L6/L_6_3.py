class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"Wage": wage, "Bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Работник: {self.name} {self.surname} {self.position}')

    def get_total_income(self):
        print(f'Доход: {self._income.get("Wage") + self._income.get("Bonus")}')


a = input('Введите Имя работника: ')
b = input('Введите Фамилию работника: ')
c = input('Введите Должность работника: ')
d = int(input('Введите Оклад работника: '))
e = int(input('Введите Премию работника: '))

worker = Position(a, b, c, d, e)
worker.get_full_name()
worker.get_total_income()
