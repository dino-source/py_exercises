import copy

def display(matrix: list[list[int]]) -> None:
    for row in matrix:
        for col in row:
            print(col, end=' ')
        print()
    print()


def create_matrix(row: int, col: int) -> list[list[int]]:
    matrix = []
    arr = []
    for _ in range(row):
        arr.append(0)
    for _ in range(col):
        matrix.append(copy.copy(arr))
    return matrix


def get_matrix(str_1: str, str_2: str) -> list[list[int]]:
    matrix = create_matrix(len(str_1), len(str_2))
    for i in range(max(len(str_1), len(str_2))):
        if str_1[i] == str_2[i]:
            matrix[i][i] = matrix[i-1][i-1] + 1
    return matrix


matrix = get_matrix("dish", "fish")
display(matrix)
