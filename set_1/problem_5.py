def nth_element(A, n):
    if n > len(A) or n < 1:
        return None

    return A[n-1]

