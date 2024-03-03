from set_1 import problem_1, problem_2, problem_3, problem_4, problem_5
def test_get_sum():
    given = [1, 2, 3, 4]
    expected = 10
    actual = problem_1.get_sum(given)
    assert actual == expected

def test_get_sum_N():
    given = 4
    expected = 10
    actual = problem_1.get_sum_N(given)
    assert actual == expected

# Get multiplication of N (1*2*3*4 … *N)
def test_get_multiplication():
    given = 4
    expected = 24
    actual = problem_2.get_mul_of_N(given)

# Check if a number is even or odd
def test_is_even_true():
    given = 6
    expected = True
    actual = problem_3.is_even(given)
    assert actual == expected

def test_is_even_flase():
    given = 7
    expected = False
    actual = problem_3.is_even(given)
    assert actual == expected

def test_is_odd_true():
    given = 5
    expected = True
    actual = problem_3.is_odd(given)
    assert actual == expected

def test_is_odd_flase():
    given = 6
    expected = False
    actual = problem_3.is_odd(given)
    assert actual == expected

# Find number of even and number odd numbers in a list
def test_num_of_even():
    given = [2, 4, 7, 11, 21, 40]
    expected = 3
    actual = problem_4.num_of_even(given)
    assert actual == expected

def test_num_of_odd():
    given = [2, 4, 7, 11, 21, 40, 43]
    expected = 4
    actual = problem_4.num_of_odd(given)
    assert actual == expected

# Find nth element in a list ,
# when nth element not exists, return None
def test_nth_element_not_exists():
    given_A = [2, 7, 12, 32, 35, 50]
    given_N = 7
    expected = None
    actual = problem_5.nth_element(given_A, given_N)
    assert actual == expected

#
def test_nth_element_if_less_than_1():
    given_A = [2, 7, 12, 32, 35, 50]
    given_N = -1
    expected = None
    actual = problem_5.nth_element(given_A, given_N)
    assert actual == expected

def test_nth_element_if_exists():
    given_A = [2, 7, 12, 32, 35, 50]
    given_N = 1
    expected = 2
    actual = problem_5.nth_element(given_A, given_N)
    assert actual == expected


