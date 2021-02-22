class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go_car(self):
        return f'Машина {self.name} поехала'

    def stop_car(self):
        return f'Машина {self.name} остановилась'

    def turn_right(self):
        return f'Машина {self.name} повернул на право'

    def turn_left(self):
        return f'Машина {self.name} повернул на лево'

    def show_speed(self):
        return f'Скорость {self.name} {self.speed}км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'{self.name} {self.color} {self.speed} {self.is_police}')

    def show_speed(self):
        if self.speed > 60:
            return f'Машина {self.name} {self.speed}км/ч превышает скорость'
        else:
            return f'Скорость {self.name} {self.speed}км/ч'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'{self.name} {self.color} {self.speed} {self.is_police}')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'{self.name} {self.color} {self.speed} {self.is_police}')

    def show_speed(self):
        if self.speed > 40:
            return f'Машина {self.name} {self.speed}км/ч превышает скорость'
        else:
            return f'Скорость {self.name} {self.speed}км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'{self.name} {self.color} {self.speed} {self.is_police}')

    def police(self):
        if self.is_police:
            return f'{self.name} в полицейском учатске'
        else:
            return f'{self.name} не в полицейском участке'


town_car = TownCar(65, 'Синий', 'Mazda', False)
work_car = WorkCar(45, 'Жёлтый', 'Kia', False)
sport_car = SportCar(120, 'Чёрный', 'BMW', True)
police_car = PoliceCar(80, 'Белый', 'Ford', True)
print(work_car.show_speed())
print(town_car.show_speed())
print(work_car.turn_left())
print(f'{town_car.turn_right()}, {sport_car.stop_car()}')
print(f'{work_car.go_car()} как и {work_car.show_speed()}')
print(sport_car.show_speed())
print(police_car.police())
print(police_car.show_speed())
