#  Sum of Multiples

def sum_multiplies(number, mult1, mult2):

    if number < 0 or mult1 < 0 or mult2 < 0:
        raise ValueError("Input values must be positive")

    multiplesList = []

    for x in range(1, number):
        if x % mult1 == 0 or x % mult2 == 0:
            multiplesList.append(x)
        else:
            continue

    multiplesList.sort()
    return("The sum of multiples is " + str(sum(multiplesList))) and "List of multiples: " + str(multiplesList)
