def dna(s):
    return (str(s.count('A')) + ' ' + str(s.count('C')) + ' ' +
            str(s.count('G')) + ' ' + str(s.count('T')))


def dna_with_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
        return dna(str(data))


def dna_tester():
    assert (dna('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
            == '20 12 17 21')
    assert dna_with_file('original.txt') == '20 12 17 21'
    assert (dna('') == '0 0 0 0')


if __name__ == "__main__":
    dna_tester()
    print(dna_with_file('rosalind_dna.txt'))




