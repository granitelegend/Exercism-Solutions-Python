# Grains problem
# Doubling the grains starting with 1 grain, formula in closed form is 2^(n-1) with

def grains(sqre):
    if not 1 <= sqre <= 64:
        raise ValueError("square must be between 1 and 64")
    return "Square: " + str(2 ** (sqre - 1)), "Total: " + str(int((2 ** sqre - 1)))
