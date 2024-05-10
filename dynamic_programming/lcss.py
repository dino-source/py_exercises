def display(matrix: list[list[int]]) -> None:
    for row in matrix:
        for col in row:
            print(col, end=' ')
        print()
    print()


word_a = "dish"
word_b = "fish"
i = 0
j = 0
cell = [
    [0,0,0,0,],
    [0,0,0,0,], 
    [0,0,0,0,], 
    [0,0,0,0,], 
]

for _ in word_a:
    if word_a[i] == word_b[j]:
        cell[i][j] = cell[i-1][j-1] + 1
    else:
        cell[i][j] = 0
    i += 1
    j += 1

display(cell)
