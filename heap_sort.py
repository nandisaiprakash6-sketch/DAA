# Function to maintain the Max Heap property
def heapify(arr, n, i):
    largest = i          # Assume the current node is the largest
    left = 2 * i + 1     # Left child index
    right = 2 * i + 2    # Right child index

    # Check if the left child is larger than the current largest
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if the right child is larger than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the current node, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Heap Sort function
def heap_sort(arr):
    n = len(arr)

    # Step 1: Build a Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move the largest element (root) to the end
        arr[0], arr[i] = arr[i], arr[0]

        # Restore the Max Heap for the remaining elements
        heapify(arr, i, 0)


# Example
arr = [4, 10, 3, 5, 1]

print("Original Array:", arr)

heap_sort(arr)

print("Sorted Array:", arr)