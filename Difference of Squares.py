# Difference of Squares

def diff_squares(number):
    return int(sum(list(range(1,number + 1)))**2 - ((number*(number + 1)*(2*number + 1))/6))
