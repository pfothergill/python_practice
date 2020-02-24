#!/usr/bin/python3

# here is our first function
def GCcontent(dna):
    # our first function is called GCcontent and
    # accepts a single arguement called dna;
    # assume that the input is a DNA sequence encoded
    # in a string, and make sure it's all uppercase:
    dna = dna.upper()
    
    #count the occurances of each nucleotide
    numG = dna.count("G")
    numC = dna.count("C")
    numT = dna.count("T")
    numA = dna.count("A")

    return (numG + numC) / (numG + numC + numT + numA)