import numpy as np


def valid(filename):
    addresses = np.ones(4294967295, dtype=np.bool)  # 4294967295
    with open(filename) as fin:
        for line in fin:
            line = line.strip("\n")
            bits = line.split("-")
            addresses[int(bits[0]):int(bits[1]) + 1] = False
    allowed = np.nonzero(addresses)[0]
    return len(allowed), allowed[0]


if __name__ == "__main__":
    # print(valid("day20test.txt"))
    print(valid("day20in.txt"))