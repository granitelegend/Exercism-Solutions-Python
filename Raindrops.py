# Raindrops

def raindrop(number):
    rainWord = ""
    while True:
        if number % 3 == 0:
            rainWord += "Pling"
        if number % 5 == 0:
            rainWord += "Plang"
        if number % 7 == 0:
            rainWord += "Plong"
        break

    if rainWord == "":
        return str(number)
    else:
        return rainWord
