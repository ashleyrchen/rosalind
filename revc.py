def revc(s):
    lst = list(map(lambda x: revc_fun(x), s))
    lst.reverse()
    return ''.join(lst)


def revc_fun(char):
    conversion = dict({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'})
    return conversion[char]


def revc_with_file(filename):
    with open(filename, 'r') as file:
        data = file.read().strip()
        return revc(str(data))


def revc_tester():
    assert (revc('GTCA')
            == 'TGAC')
    assert revc_with_file('original_revc.txt') == 'TGAC'


if __name__ == "__main__":
    revc_tester()
    print(revc_with_file('rosalind_revc.txt'))