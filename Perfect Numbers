# Perfect Numbers

def is_perfect(number):
    if number < 0:
        raise ValueError("Classification is only possible for positive integers.")
    factorList = []
    for x in range(1, number):
        if number % x == 0:
            factorList.append(x)
    if sum(factorList) == number:
        return str(number) + " is perfect"
    elif sum(factorList) > number:
        return str(number) + " is abundant"
    elif sum(factorList) < number:
        return str(number) + " is deficient"

