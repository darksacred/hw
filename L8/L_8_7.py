# Операции с комплексными числами
class Kom_number:
    def __init__(self, kom_numb):
        self.kom_numb = kom_numb

    def __add__(self, other):
        return Kom_number(self.kom_numb + other.kom_numb)

    def __mul__(self, other):
        return Kom_number(self.kom_numb * other.kom_numb)

    def __str__(self):
        return f'{self.kom_numb}'


while True:
    try:
        kn1 = complex(input('Введите первое комплексное число: '))
        kn2 = complex(input('Введите второе комплексное число: '))
        print(kn1 + kn2)
        print(kn1 * kn2)
    except:
        continue
