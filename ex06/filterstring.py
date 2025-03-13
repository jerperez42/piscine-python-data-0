from ft_filter import ft_filter
import sys


def is_int(value: str) -> bool:
    """is_int
    Return True if value can be converted to int
    """
    try:
        int(value)
        return True
    except Exception:
        return False


def filterstring(S: str, N: int):
    """filterstring
    Outputs a list of words from S that have a length greater than N
    """
    def is_greater(N_: int) -> bool:
        return lambda x: len(x) >= N_
    f = is_greater(N)
    it = ft_filter(f, S)
    print([x for x in it])


def main():
    """ main
    Remove words bellow some length
    usage: python filterstring.py <words> <length>
    Words are separated from each other by space characters.
    Strings do not contain any special characters. (Punctuation or invisible)
    """
    ac = len(sys.argv)
    assert ac == 3 and is_int(sys.argv[2]), 'the arguments are bad'
    S = sys.argv[1].split(' ')
    N = int(sys.argv[2])
    filterstring(S, N)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
