#''' Define a function which takes two arguments: 
# A list of integers and a single integer
#  that represents an index point.'''

def adding_up_to(int_list, index):
    # If the index is out of bounds, return 0
    if index < 0 or index >= len(int_list):
        return 0
    # Base case: if the index is the last element, return that element
    if index == 0:
        return int_list[0]
    # Recursive case: return the current element plus the sum from the next index
    return adding_up_to(int_list, index - 1) + int_list[index]

# Example usage:
print(adding_up_to([1, 4, 5, 3, 12, 16], 4))  # Output: 25
print(adding_up_to([4, 3, 1, 5], 1))          # Output: 7
