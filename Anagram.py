# Anagram

def is_anagram(word):
    wordSet = set(["stone", "tones", "banana", "tons", "notes", "Seton"])
    anaSet = set([])
    for x in wordSet:
        if list(word.lower()) == list(x.lower()) or set(word.lower()) != set(x.lower()):
            continue
        else:
            anaSet.add(x)
    return anaSet

