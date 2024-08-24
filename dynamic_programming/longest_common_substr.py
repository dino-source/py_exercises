def display(matrix: list[list[int]]) -> None:
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()
    print()


def create_matrix(rows: int, cols: int) -> list[list[int]]:
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    return matrix


def get_matrix(str_1: str, str_2: str) -> list[list[int]]:
    matrix = create_matrix(len(str_1), len(str_2))
    limit = min(len(str_1), len(str_2))
    for i in range(limit):
        if str_1[i] == str_2[i]:
            matrix[i][i] = matrix[i - 1][i - 1] + 1
    return matrix


def main() -> None:
    words_to_compare = {
        "dish": "fish",
        "fish": "vista",
        "folk": "fort",
        "fosh": "fish",
    }

    for k, v in words_to_compare.items():
        print(f"{k}: {v}")
        matrix = get_matrix(k, v)
        display(matrix)


main()
