# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        smallest_value = arr[smallest_index]
        # TO-DO: find next smallest element
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                smallest_value = arr[j]
        # (hint, can do in 3 loc) 
             

        # TO-DO: swap
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = smallest_value


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for i in range(0, len(arr) -1):
            if arr[i] > arr[i + 1]:
                temp_value = arr[i]
                arr[i] = arr[i + 1]
                arr [i + 1] = temp_value
                has_swapped = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr