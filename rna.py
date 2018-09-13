def rna(t):
    return t.replace('T', 'U')


def rna_with_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
        return rna(str(data))


def rna_tester():
    assert (rna('GATGGAACTTGACTACGTAAATT')
            == 'GAUGGAACUUGACUACGUAAAUU')
    assert rna_with_file('original_rna.txt') == 'GAUGGAACUUGACUACGUAAAUU'
    assert (rna('GAAAAAGGGGGCCCCCCCCCCCCCCC') == 'GAAAAAGGGGGCCCCCCCCCCCCCCC')


if __name__ == "__main__":
    rna_tester()
    print(rna_with_file('rosalind_rna.txt'))