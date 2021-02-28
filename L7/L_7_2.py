class Coat:
    def __init__(self, size):
        self.coat_size = size / 6.5 + 0.5
        print(self.coat_size)


class Costume:
    def __init__(self, grow):
        self.cost_grow = 2 * grow + 0.3
        print(self.cost_grow)


class Clothing:
    def __init__(self):
        self.cloth_mat_coat = []
        self.cloth_mat_cost = []
        self.a = 0

    def add_coat(self, size):
        self.cloth_mat_coat.append(Coat(size))

    def add_clothing(self, grow):
        self.cloth_mat_cost.append(Costume(grow))

    def result(self):
        res = 0
        res1 = 0
        for el in self.cloth_mat_coat:
            res += el.coat_size

        for el in self.cloth_mat_cost:
            res1 += el.cost_grow

        res2 = res + res1
        return res2


r = Clothing()
r.add_coat(36)
r.add_coat(34)
r.add_coat(32)
r.add_clothing(40)
r.add_clothing(42)
print(r.result())
