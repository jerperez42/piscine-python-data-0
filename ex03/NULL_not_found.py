# https://en.wikipedia.org/wiki/Null_(mathematics)
# In mathematics, the word null [...] is often associated
# with the concept of zero, or with the concept of nothing.
# It is used in varying contexts from "having zero members
# in a set" [...] to "having a value of zero"

def NULL_not_found(object: any) -> int:
    t = type(object)
    isNull = 1 if (object == t() or object != object) else 0
    if 1 == isNull:
        print(t)
        return 0
    return 1


"""
def NULL_not_found(object: any) -> int:
    t = type(object)
    isNull = 1 if (object == t() or object != object) else 0
    if 1 == isNull:
        print(f"{object} {t}")
        return 0
    return 1
"""
