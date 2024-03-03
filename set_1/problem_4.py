# Find number of even and number odd numbers in a list
from set_1.problem_3 import is_even, is_odd


def num_of_even(A):
    count = 0
    for num in A:
        if is_even(num):
            count += 1
    return count


def num_of_odd(A):
    count = 0
    for num in A:
        if is_odd(num):
            count += 1
    return count

