def diagonal_difference(arr):
    reverse_arr = arr[::-1]
    diagonal_one = []
    diagonal_two = []

    for index, row in enumerate(arr):
        diagonal_one.append(row[index] if index < len(row) else 0)
        diagonal_two.append(reverse_arr[index][index] if index < len(reverse_arr[index]) else 0)

    value_one = sum(diagonal_one)
    value_two = sum(diagonal_two)


    return abs(value_one - value_two)

# Ejemplo de uso
matrix =  [
    [3],
    [11 ,2, 4],
    [4 ,5, 6],
    [10 ,8 ,-12]
]
result = diagonal_difference(matrix)
print(result)  # Output: 0
