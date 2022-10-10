# Pangram problem (not so original solution using sets and no imports)
# The problem can be reduced to sets, due to it removing duplicates and thus being able to compare the sets since
# a letter should only appear once, the cardinality of both sets should be the same for the word to be a pangram.

def is_pangram(word):
    return len(set("abcdefghijklmnopqrstuvwxyz")) == len(set((word.lower()).replace(" ", "").replace(",", "")))

