# Get multiplication of N (1*2*3*4 … *N)

def get_mul_of_N(n):
    total = 1
    for num in range(1, n+1):
        total = total * num

    return total
