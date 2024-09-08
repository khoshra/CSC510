'''
Sorting module
'''


def selection_sort(arr):
    '''
    selection sort
    :return sorted array having numbers increasing order
    '''
    n = len(arr)
    for i in range(n):
        lowest_index = i
        for j in range(n):
            if arr[j] < arr[lowest_index]:
                lowest_index = j

        arr[lowest_index] = arr[i]
        arr[i] = arr[lowest_index]
        n = n - 1

    return arr


arr_in = [5, 3, 2, 1, 8, 10, 11, 9, 23]

arr_out = selection_sort(arr_in)

print(arr_out)
