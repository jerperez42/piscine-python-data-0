import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".--- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}


def isalnumorspace(txt: str):
    """isalnumorspace
    """
    for c in txt:
        if c.isalnum():
            pass
        elif ' ' == c:
            pass
        else:
            return False
    return True


def sos(txt: str):
    """sos
    prints morse code
    """
    morsecode = dict(
        (ord(key.upper()), value) for (key, value) in NESTED_MORSE.items())
    txt = txt.upper().translate(morsecode)
    print(txt)


def to_tl_dic(char_dic: dict) -> dict:
    """to_tl_dic
    """
    return dict((ord(key.upper()), value) for (key, value) in char_dic.items())


def main():
    """ main
    Encodes text into Morse Code.
    usage: python sos.py <text>
    """
    ac = len(sys.argv)
    assert ac == 2 and isalnumorspace(sys.argv[1]), 'the arguments are bad'
    text = sys.argv[1]
    sos(text)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
