# Isogram problem

def is_isogram(word):
    return len(set(word.lower())) == len(list(word.lower()))
