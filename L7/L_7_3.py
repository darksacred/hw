class Cell:

    def __init__(self, cell):
        self.cell = cell

    def make_order(self, num_cell):
        row = ''
        for i in range(int(self.cell / num_cell)):
            row += f'{"*" * num_cell} \\n '
        row += f'{"*" * (self.cell % num_cell)}'
        return row

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        resut = self.cell - other.cell
        if resut <= 0:
            return f'Клетки погибли'
        else:
            return resut

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __floordiv__(self, other):
        return Cell(self.cell / other.cell)

    def __str__(self):
        return f"кол-во клеток ({self.cell})"


cell1 = Cell(18)
cell2 = Cell(9)
print(f'В первой пробирке {cell1}')
print(f'Во второй пробирке {cell2}')
print(f'В сумме {cell1 + cell2}')
print(cell1.make_order(5))
print(cell2.make_order(3))
print(f'Разница в {cell1 - cell2}')
print(cell1 * cell2)
print(cell1 // cell2)
