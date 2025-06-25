def myPow(x: float, n: int) -> float:
    N = n
    if N < 0:
        x = 1 / x
        N = -N

    result = 1
    while N:
        if N % 2 == 1:
            result *= x
        x *= x
        N //= 2
    return result
