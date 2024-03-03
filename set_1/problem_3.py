# Check if a number is even or odd
def is_even(num):
    if num % 2 == 0:
        return True
    return False
def is_odd(num):
    return not is_even(num)
