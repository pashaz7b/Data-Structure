class SparseMatrix:

    def __init__(self, rowcount, columncount):
        self.rowcount = rowcount
        self.columncount = columncount
        self.sparse_matrix_list = []
        self.valuecount = 0
        self.sparse_matrix_list.append([self.rowcount, self.columncount, self.valuecount])

    def insert(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value
        self.valuecount += 1
        self.sparse_matrix_list[0] = ([self.rowcount, self.columncount, self.valuecount])
        self.sparse_matrix_list.append([self.row, self.column, self.value])

    def transpose(self):
        transposed_matrix = [[0, 0, 0] for i in range(self.valuecount + 1)]

        for i in range(self.valuecount + 1):
            transposed_matrix[i][0] = self.sparse_matrix_list[i][1]
            transposed_matrix[i][1] = self.sparse_matrix_list[i][0]
            transposed_matrix[i][2] = self.sparse_matrix_list[i][2]

        sorted_transposed = [transposed_matrix[0]]
        transposed_matrix.pop(0)

        sorted_transposed += sorted(transposed_matrix, key=lambda x: x[0])

        return sorted_transposed

    def add(self, other_matrix):
        if (self.rowcount != other_matrix.rowcount or self.columncount != other_matrix.columncount):
            raise Exception("can't be added")

        else:
            valuecountUnited = 0
            united_matrix = [[self.rowcount, self.columncount, valuecountUnited]]

            for item1 in self.sparse_matrix_list[1:]:
                is_alone = True
                for item2 in other_matrix.sparse_matrix_list[1:]:
                    if (item1[0] == item2[0] and item1[1] == item2[1]):
                        united_matrix.append([item1[0], item1[1], item1[2] + item2[2]])
                        is_alone = False
                        valuecountUnited += 1
                        other_matrix.sparse_matrix_list.remove(item2)

                if (is_alone):
                    united_matrix.append([item1[0], item1[1], item1[2]])
                    valuecountUnited += 1

            for element in other_matrix.sparse_matrix_list[1:]:
                united_matrix.append(element)
                valuecountUnited += 1

            united_matrix[0][2] = valuecountUnited
            sorted_united = [united_matrix[0]]
            sorted_united += sorted(united_matrix[1:], key=lambda x: x[0])

            return sorted_united

    def multiply(self):
        pass
