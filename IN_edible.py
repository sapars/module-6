from MD import *


class Plant:
    def __init__(self, name = "tree", edible=False):
        self.edible = edible
        self.name = name


class Animal:
    def __init__(self, name='omnibeast', alive=True, fed=False):
        self.alive = alive
        self.fed = fed
        self.name = name

    def eat(self, food: Plant):
        print(f'{self.name} съел {food.name}')
        if food.edible:
            self.fed = True
            self.alive = True
        else:
            self.fed = False
            self.alive = False


class Mammal(Animal):
    def __init__(self, name='platypus'):
        super().__init__(name)


class Predator(Animal):
    def __init__(self, name='weasel'):
        super().__init__(name)


class Flower(Plant):
    def __init__(self, name='lilly', edible=False):
        super().__init__(name, edible)


class Fruit(Plant):
    def __init__(self, name='tomato', edible = True):
        super().__init__(name, edible)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
