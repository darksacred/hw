class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def rash_mass(self):
        mass = self.__length * self.__width * 25 * 5
        print(f'Масса асфальта: {mass}т')


a = int(input('Введите желаемую длину: '))
b = int(input('Введите желаемую ширину: '))
road = Road(a, b)
road.rash_mass()
