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
    print("The First Sparse Matrix:")
    matrix1 = SparseMatrix(4, 4)
    matrix1.insert(1, 2, 10)
    matrix1.insert(1, 4, 12)
    matrix1.insert(3, 3, 5)
    matrix1.insert(4, 1, 15)
    matrix1.insert(4, 2, 12)
    print_custom_object(matrix1)

    print("\nTranspose Of First Sparse Matrix:")
    transposed_matrix = matrix1.transpose()
    print_custom(transposed_matrix)

    print("\nThe Second Sparse Matrix:")
    matrix2 = SparseMatrix(4, 4)
    matrix2.insert(1, 3, 8)
    matrix2.insert(2, 4, 23)
    matrix2.insert(3, 3, 9)
    matrix2.insert(4, 1, 20)
    matrix2.insert(4, 2, 25)
    print_custom_object(matrix2)

    print("\nAddition OF First And Second Sparse Matrix:")
    addition_output = matrix1.add(matrix2)
    print_custom(addition_output)

    print("\nMultiplication Of First And Second Sparse Matrix:")
    multiplication_output = matrix1.multiply(matrix2)
    print_custom(multiplication_output)


if __name__ == '__main__':
    main()
