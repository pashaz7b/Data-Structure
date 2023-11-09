from SparseMatrix import *


def print_custom_object(input_matrix: SparseMatrix):
    for item in input_matrix.sparse_matrix_list:
        a, b, c = item
        print("|", a, b, c, "|")


def print_custom(input_matrix):
    for item in input_matrix:
        a, b, c = item
        print("|", a, b, c, "|")


def main():
    matrix1 = SparseMatrix(4, 5)
    matrix1.insert(0, 4, 8)
    matrix1.insert(1, 1, 9)
    matrix1.insert(2, 3, 3)
    print_custom_object(matrix1)

    print()

    transposed_matrix = matrix1.transpose()
    print_custom(transposed_matrix)

    print()

    matrix2 = SparseMatrix(4, 5)
    matrix2.insert(3, 0, 8)
    matrix2.insert(1, 2, 9)
    matrix2.insert(2, 3, 3)
    output = matrix1.add(matrix2)
    print_custom(output)


if __name__ == '__main__':
    main()
