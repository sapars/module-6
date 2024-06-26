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
            self.fed = True
            self.alive = True
        else:
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

m = Mammal("Lion")
p = Predator("Wolf")
c = Fruit('cherry')
t= Flower()

p.eat(t)

print(p.fed, p.name, t.name)