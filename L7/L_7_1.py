class Matrix:
    def __init__(self, list_1, list_2):
        self.matr = [list_1, list_2]
        self.list_1 = list_1
        self.list_2 = list_2

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.list_1]))

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


my_matrix = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]], [[3, 2, 11], [4, 7, 87], [23, 7, 87]])
print(my_matrix.__str__())
print(my_matrix.__add__())
