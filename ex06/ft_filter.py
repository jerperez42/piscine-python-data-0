import typing


# you should use list comprehensions to recode your ft_filter
def ft_filter(
    function: typing.Callable | None,
    iterable: typing.Iterable
) -> typing.Iterable:
    """filter(function or None, iterable) --> list_iterator object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if (function is None):
        return iter([x for x in iterable if x])
    return iter([x for x in iterable if function(x)])

# print(filter.__doc__)
# print(ft_filter.__doc__)

# def f(x):
#     return x != 2

# print(ft_filter(f, [0,1,2,3]))

# print(ft_filter(None, [0,1,2,3]))

# print(filter(f, [0,1,2,3]))

# print(filter(None, [0,1,2,3]))
