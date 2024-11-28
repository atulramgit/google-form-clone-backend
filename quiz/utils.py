import string
import random

def generateRandomCode(n=7):
    res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=n))

    return res