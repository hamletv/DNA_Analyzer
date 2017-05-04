sample = ['GTA','GGG','CAC']

#method opens and reads dna_file then take every line in dna_file (f) add it to dna_data variable.
def read_dna(dna_file):
    dna_data = ''
    with open(dna_file, 'r') as f:
      for line in f:
        dna_data += line
    return dna_data

#method takes DNA strands slices them into codons and passed to list named codons.
def dna_codons(dna):
  codons = []
  for i in range(0, len(dna), 3):
    if (i + 3) < len(dna): #checks that items added to codons list must be 3 letters long.
      codons.append(dna[i:i+3]) #check slicing, must give 3 letters/codon starting with 0 index.
  return codons

#method matches codons from suspect dna to sample dna found at scene; counts number of matches.
def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon in sample:
        matches += 1
  return matches

#method takes above methods to check suspects and determine whose dna is sample/crime scene dna.
def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample) #read suspect dna, store into variable.
  codons = dna_codons(dna_data) #pass variable from read_dna to slice into codons and pass into list.
  num_matches = match_dna(codons) #count number of matches from sample and suspect dna.

  if num_matches >= 3:
    print 'There are %s matching codons. The investigation should continue.' % (num_matches)
  else:
    print 'There are %s matching codons. Further investigation will not be needed. This suspect can be released.' % (num_matches)

is_criminal('suspect1.txt')
is_criminal('suspect2.txt')
is_criminal('suspect3.txt')
