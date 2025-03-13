def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    tot = len(lst)
    width = 80  # no way* to get terminal len without function
    i = 0
    for x in lst:
        i += 1
        ratio = i / tot
        pct = 100 * ratio
        bar = "█" * int(width * ratio)
        # no way* to get time without function
        print(f"\r{pct: >3.0f}%|{bar: <{width}}| {i}/{tot}", end='')
        if (i == tot):
            print()
        yield
