# step-1: picking the smallest element from the unsorted part of the array
# step-2: swapping it with the first unsorted element
# step-3: repeat the process for the rest of the array



def selection_sort(arr: list) -> list:  # Time Complexity: O(n^2), Space Complexity: O(1)
    n = len(arr)

    for idx in range(n-1):
        min_ele = idx
        for idx_j in range(idx+1, n):
            if arr[min_ele] > arr[idx_j]:
                min_ele = idx_j
        arr[idx], arr[min_ele] = arr[min_ele], arr[idx]
    return arr


if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)
    # Output: Sorted array: [11, 12, 22, 25, 64]




