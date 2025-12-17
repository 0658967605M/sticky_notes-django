# '''Implement this search algorithm to search for the number 9. Add a 
# comment to explain why you think this algorithm was a good choice. 
# Using the following list: [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]''' 
def linear_search(arr, target): #'''Linear search is a good choice for unsorted lists
    for i in range(len(arr)):   # because it checks each element one by one'''
        if arr[i] == target:
            return i
    return -1

# Linear search on unsorted list
print("Linear search (unsorted):", \
 linear_search(numbers, 9))  # Output: 10

# Example usage:
numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
print(linear_search(numbers, 9))  # Output: 10

# Research and implement the Insertion sort on this list:
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Sort the list
sorted_numbers = insertion_sort(numbers.copy())
print("Sorted list:", sorted_numbers)


# '''Implement a searching algorithm you haven’t tried yet in this task on the 
# sorted list to find the number 9. Add a comment to explain where you would 
# use this algorithm in the real world.'''
def binary_search(arr, target): #'''Binary search is efficient for large, sorted datasets
    low = 0         # because it reduces the search space by half each step.'''
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Binary search on sorted list
print("Binary search (sorted):", \
binary_search(sorted_numbers, 9))  # Output: index of 9 in sorted list