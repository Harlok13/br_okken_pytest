TEST_DATA = ('abcaa cbanada',
             'acavv vavacda',
             'asd asjne',
             'asd asda',
             'abbsa absaar',
             'ansans afnsaaanndfks')

EXPECTED_VALUE = (0, 0, 0, 1, 0, 1)


def check_substr_in_string(sub_strng: str, strng: str) -> int:
    """Проверить подстроку в строке."""
    from collections import Counter
    object_c1 = Counter(sub_strng)
    object_c2 = Counter(strng)
    for key in object_c1:
        if object_c1.get(key, False) > object_c2.get(key, False):
            break
    else:
        return 1
    return 0


def foo(a, b):
    for el in b:
        if a and el == a[0]:
            a = a[1:]
    return 0 if a else 1

if __name__ == '__main__':
    for expected, test in enumerate(TEST_DATA):
        sub_strng, strng = test.split()
        # assert check_substr_in_string(sub_strng, strng) == EXPECTED_VALUE[expected]
        assert foo(sub_strng, strng) == EXPECTED_VALUE[expected]

