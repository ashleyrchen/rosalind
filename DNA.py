def dna(s):
    dna_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for char in s:
        if char == 'A':
            dna_dict['A'] += 1
        elif char == 'C':
            dna_dict['C'] += 1
        elif char == 'G':
            dna_dict['G'] += 1
        elif char == 'T':
            dna_dict['T'] += 1

    return (str(dna_dict['A']) + ' ' + str(dna_dict['C']) + ' ' +
            str(dna_dict['G']) + ' ' + str(dna_dict['T']))


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




