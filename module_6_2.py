COLORS: set = {'white',
               'black',
               'red',
               'green',
               'blue',
               'cyan',
               'magenta',
               'yellow'
               }


class Vehicle:
    __COLOR_VARIANTS = list(COLORS)

    def __init__(self, owner: str = 'Owen', model: str = "SSL", power: int = 100, color: str = 'white'):
        self.owner = owner
        self.__model = model
        self.__engine_power = power
        if color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = color
        else:
            self.__color = 'white'

    def get_model(self):
        print(f'Модель: {self.__model}')
        return self.__model

    def get_horsepower(self):
        print((f'Мощность двигателя: {self.__engine_power}'))
        return self.__engine_power

    def get_color(self):
        print(f'Цвет: {self.__color}')
        return self.__color

    def print_info(self):
        print(f'Владелец: {self.owner}')
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print('_________________')

    def set_color(self, color: str='red'):
        if color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = color
        else:
            print(f'Невозможно покрасить в {color}')



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()
