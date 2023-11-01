from SparseMatrix import *


def main():
    matrix1 = SparseMatrix(1, 6)
    matrix1.insert(1, 2, 3)
    matrix1.insert(1, 4, 6)
    matrix1.insert(1, 5, 9)
    matrix1.print_whole_matrix()


if __name__ == '__main__':
    main()
