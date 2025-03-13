import sys


def isInt(value: str) -> bool:
    try:
        int(value)
        return True
    except Exception:
        return False


def whatis(num: int):
    if (0 == (num % 2)):
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main():
    sys.tracebacklimit = 0
    assert len(sys.argv) < 3, "more than one argument is provided"
    assert len(sys.argv) == 2, "one argument must be provided"
    num = sys.argv[1]
    assert isInt(num) is True, "argument is not an integer"
    whatis(int(num))


if __name__ == "__main__":
    main()
