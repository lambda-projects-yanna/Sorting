def selection_sort( arr ):
    # loop through the array once for each element 
    for i in range(0, len(arr) - 1):
        # find smallest element in array 
        for i in range(0, len(arr)-1):
            # if current element is bigger than one to
            # the right of it:
            if arr[i] > arr[i+1]:
                # swap smaller element to the left
                arr[i], arr[i+1] = arr[i+1], arr[i]
                print(arr)
    return arr

test = [5, 2, 4, 1, 7, 3]
selection_sort(test)



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr