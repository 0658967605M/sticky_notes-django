
# Modify the merge sort algorithm provided in the example usage section 
# above to order a list of strings by string length from the longest to the 
# shortest string.
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if len(left_half[i]) > len(right_half[j]):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Example usage:
string_list1 = ["apple", "banana", "cherry", "date", "fig", "grape"]
string_list2 = ["elephant", "dog", "cat", "zebra", "lion", "tiger"]
string_list3 = ["red", "blue", "black", "yellow", "white", "orange"]

print(merge_sort(string_list1))
print(merge_sort(string_list2))
print(merge_sort(string_list3))

# Run the modified Merge sort algorithm against 3 string lists of your choice.
# Please ensure that each of your chosen lists is not sorted and has a length of
# at least 10 string elements.
string_list4 = ["strawberry", "apple", "mango", "orange", "blueberry", "grapes", "raspberry", "coconut", "banana", "pineapple"]
string_list5 = ["carrot", "pumpkin", "", "cauliflower", "spinach", "kale", "cabbage", "lettuce", "pepper", "onion"]
string_list6 = ["Mercedes", "BMW", "Audi", "Hondai", "Lamborghini", "Ferrari", "Tesla", "Ford", "volkswagen", "Toyota"]

print(merge_sort(string_list4))
print(merge_sort(string_list5))
print(merge_sort(string_list6))