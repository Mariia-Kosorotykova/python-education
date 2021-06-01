"""This module implements simple basic_algorithms.

- Binary search
- Quick sort (Iterative)
- Recursive factorial implementation
"""

def binary_search(current_list, item):
    """Implements binary search, returns index of element in list"""
    first_idx = 0
    last_idx = len(current_list) - 1

    while first_idx <= last_idx:
        middle_idx = (first_idx + last_idx)//2
        desired_element = current_list[middle_idx]

        if desired_element == item:
            return middle_idx

        if desired_element < item:
            first_idx = middle_idx + 1
        else:
            last_idx = middle_idx - 1
    return None

def factorial(number):
    if number < 0:
        raise Exception("Number must be >= 0!")
    if number in (0, 1):
        return 1
    else:
        return number * factorial(number-1)

if __name__ == "__main__":
    # testing
    list_ex = [1, 3, 5, 7, 9]
    print(binary_search(list_ex, 1))
    print(binary_search(list_ex, 7))
    print(binary_search(list_ex, 10))

    print(factorial(4))
    print(factorial(0))
    print(factorial(-10))

