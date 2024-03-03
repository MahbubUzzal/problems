
# Get sum of N (1+2+3+4 … + N)
def get_sum(A):
    total = 0
    for val in A:
        total = total + val
    return total

def get_sum_N(N):
    total = 0
    for number in range(1, N+1):
        total = total + number
    return total
