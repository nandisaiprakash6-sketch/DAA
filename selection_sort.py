def selection_sort(arr):
    n = len(arr)

    # Traverse through the entire array
    for i in range(n):

        # Assume the current index has the smallest element
        min_index = i

        # Find the index of the smallest element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the smallest element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Example
arr = [64, 25, 12, 22, 11]

print("Original Array:", arr)

selection_sort(arr)

print("Sorted Array:", arr)