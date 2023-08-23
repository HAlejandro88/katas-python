


def unique_array(array):
    unique_array_sum = []
    for i in array:
        if isinstance(i, list):
            unique_array_sum.extend(unique_array(i))
        else:
            unique_array_sum.append(i)
    return unique_array_sum        



print(unique_array([1,2,3,[3,5,6,7,7, [1,2,3,[4,5,6]]], 3,[4,6],[[2,4,5],0,9] ]))