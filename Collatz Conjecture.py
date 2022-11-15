
# Collatz Conjecture

def collatz_conjecture(n):
    """
    Returns the amount of steps for the Collatz algorithm to reach 1.
    :param n: int
    :return: int
    """

    if n <= 0:
        raise ValueError("Only positive integers are allowed")

    steps = 0

    while n != 1:
        if n % 2 == 0:
            n /= 2
            steps += 1
        else:
            n = 3*n + 1
            steps += 1

    return int(steps)
