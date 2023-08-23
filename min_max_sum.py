
import sys

def miniMaxSum(arr):
    # Write your code here
    sums = []
    aux = arr.copy()
    for num in range(len(arr)):
        aux = arr.copy()
        aux.pop(num)
        sums.append(sum(aux))
    
    min_value = min(sums)
    max_value = max(sums)

    #return sys.stdout.write(f'{min_value} {max_value}')
    return f'{min_value} {max_value}'



print(miniMaxSum([1, 2, 3, 4, 5]))