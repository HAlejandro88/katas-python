

def birthay_cake_candles(array):
    unique_array = list(set(array))

    count_number = len(list(filter(lambda x: x == unique_array[0], array)))

    for item in unique_array:
        if count_number > len(list(filter(lambda x: x == item, array))):
            count_number = count_number
        else: 
            count_number = len(list(filter(lambda x: x == item, array)))
    
    return count_number


print(birthay_cake_candles([1,1,1,2,2,2,3,3,2,2,4]))