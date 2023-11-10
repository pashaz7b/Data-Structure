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

        sorted_transposed += sorted(transposed_matrix, key=lambda x: (x[0], x[1]))

        return sorted_transposed

    def add(self, other_matrix):

        copyOfSelf = self.sparse_matrix_list.copy()
        copyofOther = other_matrix.sparse_matrix_list.copy()

        if (self.rowcount != other_matrix.rowcount or self.columncount != other_matrix.columncount):
            raise Exception("Matrix dimensions mismatch. The matrices cannot be added.")

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
            sorted_united += sorted(united_matrix[1:], key=lambda x: (x[0], x[1]))

            for x in sorted_united:
                if (x[2] == 0):
                    sorted_united.remove(x)
                    valuecountUnited -= 1
                    sorted_united[0][2] = valuecountUnited

            self.sparse_matrix_list = copyOfSelf
            other_matrix.sparse_matrix_list = copyofOther

            return sorted_united

    def multiply(self, other_matrix):
        if self.columncount != other_matrix.rowcount:
            raise Exception(
                "The number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication.")

        result_matrix = SparseMatrix(self.rowcount, other_matrix.columncount)

        for i in range(1, len(self.sparse_matrix_list)):
            for j in range(1, len(other_matrix.sparse_matrix_list)):
                if self.sparse_matrix_list[i][1] == other_matrix.sparse_matrix_list[j][0]:
                    result_matrix.insert(self.sparse_matrix_list[i][0], other_matrix.sparse_matrix_list[j][1],
                                         self.sparse_matrix_list[i][2] * other_matrix.sparse_matrix_list[j][2])

        sorted_result = [result_matrix.sparse_matrix_list[0]]
        result_matrix.sparse_matrix_list.pop(0)
        sorted_result += sorted(result_matrix.sparse_matrix_list, key=lambda x: (x[0], x[1]))
        return sorted_result
