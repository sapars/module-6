class Plant:
    def __init__(self, name = "tree", edible=False):
        self.edible = edible
        self.name = name


class Animal:
    def __init__(self, name, alive=True, fed=False):
        self.alive = alive
        self.fed = fed
        self.name = name

    def eat(self, food: Plant):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
            self.alive = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.fed = False
            self.alive = False


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    def __init__(self, name = 'lilly', edible=False):
        super().__init__(name, edible)


class Fruit(Plant):
    def __init__(self, name, edible = True):
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
p.eat(t)

print(p.fed, p.name, t.name)
