# Etl

def etl(word):
    sumLetter = 0
    scoreLetter = dict.fromkeys(["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"], 1)
    scoreLetter.update(scoreLetter.fromkeys(["d", "g"], 2))
    scoreLetter.update(scoreLetter.fromkeys(["b", "c", "m", "p"], 3))
    scoreLetter.update(scoreLetter.fromkeys(["f", "h", "v", "w", "y"], 4))
    scoreLetter.update(scoreLetter.fromkeys(["k"], 5))
    scoreLetter.update(scoreLetter.fromkeys(["j", "x"], 8))
    scoreLetter.update(scoreLetter.fromkeys(["q", "z"], 10))
    for x in word.lower():
        print(scoreLetter.get(x), x)
        sumLetter = sumLetter + scoreLetter.get(x)
    return sumLetter
