# step-1: start from the second element from the array/list assuming the first element is already sorted.
# step-2: compare the current element with left side elements.
# step-3: shift all the elements to the right until the current element is in the correct position.
# step-4: insert the current element in the correct position, where all the elements to the left are smaller and all the elements to the right are larger.
# step-5: move to the next element and repeat the process until the end of the array/list is reached.


def insertion_sort(arr:list)->list:
    n = len(arr)

    for idx in range(1,n): # start from the second element
        current_element = arr[idx]
        j = idx - 1
        while j >= 0 and arr[j] > current_element:
            arr[j + 1] = arr[j]
            j-=1
        arr[j+1] = current_element

    return arr


# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    sorted_arr = insertion_sort(arr)
    print("Sorted array is:", sorted_arr)