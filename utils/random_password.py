import random
from string import ascii_uppercase, ascii_lowercase, hexdigits


def random_password(n=10):
    pw = ""
    for i in range(n):
        pw += (
            random.choice(hexdigits)
            + random.choice(ascii_uppercase)
            + random.choice(ascii_lowercase)
            + random.choice("~!@#$%^&*()+")
        )

    return pw[:n]
