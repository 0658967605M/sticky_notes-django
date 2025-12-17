# Define a function that takes a single argument: 
# a. A list of integers
def find_largest_number(int_list):
    # Base case: if the list is empty, return None
    if not int_list:
        return None
    # Recursive case: find the largest number in the rest of the list
    largest = find_largest_number(int_list[1:])
    # If the largest number in the rest of the list is None,
    # return the first element
    if largest is None:
        return int_list[0]
    # return the larger of the first element and the largest number found
    return max(int_list[0], largest)

print(find_largest_number([1, 4, 5, 3]))  # Output: 5
print(find_largest_number([3, 1, 6, 8, 2, 4, 5]))  # Output: 8