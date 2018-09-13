def revc(s):
    s = map(lambda x: revc_fun(x), s)
    lst = list(s)
    lst.reverse()
    return ''.join(lst)


def revc_fun(char):
    if char == 'A':
        return 'T'
    elif char == 'T':
        return 'A'
    elif char == 'C':
        return 'G'
    elif char == 'G':
        return 'C'
    else:
        return char


def revc_with_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
        return revc(str(data))


def revc_tester():
    assert (revc('GTCA')
            == 'TGAC')
    assert revc_with_file('original_revc.txt') == 'TGAC'


if __name__ == "__main__":
    # print(revc('GTCA'))
    revc_tester()
    #print(revc_with_file('rosalind_revc.txt'))