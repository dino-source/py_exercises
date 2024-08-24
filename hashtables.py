def map_chars_to_prime_numbers():
    chars = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
        " ",
    ]
    pnums = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
        103,
        107,
        109,
        113,
        127,
        131,
        139,
        149,
        151,
        157,
        163,
        167,
        173,
        179,
        181,
        191,
        193,
        197,
        199,
        211,
        223,
        227,
        229,
        233,
        239,
        241,
        251,
    ]
    return dict(zip(chars, pnums))


def hashfunc(name: str) -> int:
    abc = map_chars_to_prime_numbers()
    sum = 0
    for ch in name:
        sum += abc[ch]
    return sum % len(name)


names = [
    "Bill Ward",
    "Adrian Smith",
    "Glenn Hughes",
    "Ken Hensley",
    "Mick Box",
    "John Bonham",
    "Robert Plant",
    "Ian Paice",
    "Ian Gillan",
    "Jimmy Page",
    "David Byron",
    "Gary Thain",
    "Don Airey",
    "Dan Swano",
    "Ozzy Osbourne",
]


def fill_hashtable(names: list) -> list:
    my_hashtable = [
        [],
    ] * 16
    for name in names:
        index = hashfunc(name)
        if not my_hashtable[index]:
            my_hashtable[index] = [
                name,
            ]
        else:
            my_hashtable[index].append(name)
    return my_hashtable


def main():
    hashtable = fill_hashtable(names)
    i = 0
    for bucket in hashtable:
        print(f"{i}. {bucket}")
        i += 1


main()
