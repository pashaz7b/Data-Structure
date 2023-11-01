class SparseMatrix:
    sparse_matrix_list = []
    valuecount = 0

    def __init__(self, rowcount, columncount):
        self.rowcount = rowcount
        self.columncount = columncount
        self.sparse_matrix_list.append((self.rowcount, self.columncount, self.valuecount))

    def insert(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value
        self.valuecount += 1
        self.sparse_matrix_list[0] = ((self.rowcount, self.columncount, self.valuecount))
        self.sparse_matrix_list.append((self.row, self.column, self.value))

    def add(self):
        pass

    def transpose(self):
        pass

    def multiply(self):
        pass

    def print_whole_matrix(self):
        for item in self.sparse_matrix_list:
            a, b, c = item
            print("|", a, b, c, "|")
