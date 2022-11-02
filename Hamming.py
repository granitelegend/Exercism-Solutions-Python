# Hamming problem

def hamming(dna1, dna2):
    hamDist = []
    if len(dna1) != len(dna2):
        raise ValueError("Strands must be of equal length.")
    else:
        for x in range(0, len(dna1)):
            if dna1[x] != dna2[x]:
                hamDist.append(x)
            else:
                continue
    return len(hamDist)
