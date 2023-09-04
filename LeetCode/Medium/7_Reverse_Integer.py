import math

def reverse(x):
    z = 0
    c = int(math.log10(abs(x))) + 1
    for i in reversed(range(c)):
        z = z + (x // 10**i) * 10**(c - 1 - i)
        x = x - (x // (10**i) * 10**i)
    return z

if __name__ == "__main__":
    x = 123
    print(reverse(x))