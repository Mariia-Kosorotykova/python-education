"""This module implements simple basic_algorithms.

- Binary search
- Quick sort (Iterative)
- Recursive factorial implementation
"""


from random import choice

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

def qsort_recursive(current_list):
    """Implements qsort with recursive"""
    size_list = len(current_list)
    if size_list <= 1:
        return current_list

    pivot = choice(current_list)
    left_side = []
    right_side = []
    middle = []

    for element in current_list:
        if element < pivot:
            left_side.append(element)
        elif element > pivot:
            right_side.append(element)
        else:
            middle.append(element)

    return qsort_recursive(left_side) + middle + qsort_recursive(right_side)

def factorial(number):
    """This function implements the calculation of factorial number"""
    if number < 0:
        raise Exception("Number must be >= 0!")
    if number in (0, 1):
        return 1
    else:
        return number * factorial(number-1)

def partition(s_list, left, right):
    """Implements partition for iterative qsort"""
    pivot = left

    for i in range(left + 1, right + 1):
        if s_list[i] <= s_list[left]:
            pivot += 1
            s_list[i], s_list[pivot] = s_list[pivot], s_list[i]
    s_list[pivot], s_list[left] = s_list[left], s_list[pivot]
    return pivot

def iterative_qsort(s_list):
    """Implements iterative qsort fot current list"""
    left = 0
    right = len(s_list) - 1
    stack = [0] * (right - left + 1)
    top = -1
    top += 1
    stack[top] = left
    top += 1
    stack[top] = right

    while top >= 0:
        right = stack[top]
        top -= 1
        left = stack[top]
        top -= 1
        pivot = partition(s_list, left, right)
        if pivot - 1 > left:
            top += 1
            stack[top] = left
            top += 1
            stack[top] = pivot - 1

        if pivot + 1 < right:
            top += 1
            stack[top] = pivot + 1
            top += 1
            stack[top] = right

if __name__ == "__main__":
    # testing
    list_ex = [1, 3, 5, 7, 9]
    print(binary_search(list_ex, 1))
    print(binary_search(list_ex, 7))
    print(binary_search(list_ex, 10))

    print(factorial(4))
    print(factorial(0))
    print(factorial(-10))

    list_ex = [3, 8, 10, 1, 0, 34]

    print(qsort_recursive(list_ex))
