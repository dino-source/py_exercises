def move_zeroes_to_the_end(numbers: list[int]) -> list[int]:
    numbers.sort(key=lambda n: n==0)
    return numbers

x = [0, 1, -9, 4, 0, 6, -5, 0, 2, 3, 0]
print(move_zeroes_to_the_end(x))