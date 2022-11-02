# Rna Transcription

def rna_transcription(dna):
    newRna = ""
    rnaDict = {"G": "C", "C": "G", "T": "A", "A": "U"}
    for x in dna:
        newRna = newRna + rnaDict.get(x)
    return newRna
