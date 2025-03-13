import time

t = time.time()
print(
    "Seconds since January 1, 1970: "
    + f"{t:,.4f} or {t:.2E} in scientific notation")
print(time.strftime("%b %d %Y", time.gmtime(t)))
