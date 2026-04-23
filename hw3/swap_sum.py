def swap_sum(A, B):
    """Swaps two elements in two sorted arrays to obtain a target sum 
    difference of 10.

    Assumes that both arrays are sorted in ascending order and only 
    contain integers.

    """
    sum_a = sum(A)
    sum_b = sum(B)

    # After swapping A[i] and B[j], we need:
    # (sum_b - B[j] + A[i]) == (sum_a - A[i] + B[j]) + 10
    # which simplifies to: A[i] - B[j] = (sum_a - sum_b + 10) / 2
    needed_twice = sum_a - sum_b + 10

    if needed_twice % 2 != 0:
        return None

    target = needed_twice // 2

    i = 0
    j = 0
    len_a = len(A)
    len_b = len(B)

    while i < len_a and j < len_b:
        diff = A[i] - B[j]

        if diff == target:
            return (i, j)

        if diff < target:
            i += 1
        else:
            j += 1

    return None
