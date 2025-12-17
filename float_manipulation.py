import statistics
# '''Write a program that starts by asking the user
# to input 10 floats (these can be a combination of whole
# numbers and decimals) and store these numbers in a list.'''


def get_float_inputs():
    float_list = []
    print("Please enter 10 float numbers (whole numbers and\
     decimals are allowed):")
    while len(float_list) < 10:
        user_input = input(f"Enter float {len(float_list) + 1}: ")
        if user_input:
            try:
                float_list.append(float(user_input))
            except ValueError:
                print("Invalid input. Please enter a valid float.")
    return float_list

# Find the total of all the numbers and print the result


def print_total(float_list):
    total = sum(float_list)
    print(f"The total of all the numbers is: {total}")

# Find the index of the maximum and print the result


def print_max_index(float_list):
    max_index = float_list.index(max(float_list))
    print(f"The index of the maximum number is: {max_index}")

# Find the index of the minimum and print the result


def print_min_index(float_list):
    min_index = float_list.index(min(float_list))
    print(f"The index of the minimum number is: {min_index}")

# '''Calculate the average (mean) of the numbers and round off to two decimal
# places. Print the result.'''


def print_average(float_list):
    average = statistics.mean(float_list)
    print(f"The average of the numbers is: {average:.2f}")

# Find the median number and print the result


def print_median(float_list):
    median = statistics.median(float_list)
    print(f"The median of the numbers is: {median:.2f}")
