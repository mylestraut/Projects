
codons = {"ATT":"I", "ATC":"I", "ATA":"I",
          "CTT":"L", "CTC":"L", "CTA":"L","CTG":"L","TTA":"L","TTG":"L",
          "GTT":"V", "GTC":"V","GTA":"V","GTG":"V"
    
    }

def translate(sequence):
    result =""
    length = len(sequence)
    for i in range(0, length,3):
        codon = sequence[i:i+3]
        if codon in codons:
            result += codons[codon]
        else:
            result += "X"
    return result


def mutate(infile, character):
    infile = open(infile,'r')
    data = infile.read()
    position = data.find(character)
    return "The first occurance of {} is at {}".format(character,position)

def translate_in_file(infile):
    infile = open(infile)
    data = infile.read()
    return translate(data)

print(translate_in_file("mutatedDNA.txt"))

print(mutate("DNA.txt", "a"))
