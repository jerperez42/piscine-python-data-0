def all_thing_is_obj(object: any) -> int:
    print(type(object))
    return 42


"""
# To reproduce the exact prompt
def all_thing_is_obj(object: any) -> int:
    t = type(object)
    s = "type not found"

    if t in [list, tuple, set, dict]:
        s = f"{t.__name__} : {t}"
    elif t is str:
        s = f"{object} is in the kitchen : {t}"
    print(s.capitalize())
    return 42
"""
