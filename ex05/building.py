import sys
import string  # use sets, no functions


def print_info(text: str):
    """
    Printfs text info according to format
    """
    ch = 0
    ul = 0
    ll = 0
    pm = 0
    sp = 0
    di = 0
    for c in text:
        ch += True
        ul += c in string.ascii_uppercase
        ll += c in string.ascii_lowercase
        pm += c in string.punctuation
        sp += c in string.whitespace
        di += c in string.digits
    print(f"The text contains {ch} characters:")
    print(f"{ul} upper letters")
    print(f"{ll} lower letters")
    print(f"{pm} punctuation marks")
    print(f"{sp} spaces")
    print(f"{di} digits")


def get_text():
    """
    Gets user text
    """
    try:
        return input('What is the text to count?\n') + "\n"
    except EOFError:
        return ""


def main():
    """
    Prints text info.
    usage: python building.py [<text>]
    """
    ac = len(sys.argv)
    assert ac <= 2, 'more than one argument was provided'
    if (ac < 2 or sys.argv[1] == ''):
        text = get_text()
    else:
        text = sys.argv[1]
    print_info(text)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(e)
    except Exception as e:
        print(f"Exception: {e}")
