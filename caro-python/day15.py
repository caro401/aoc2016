input_str = """Disc #1 has 17 positions; at time=0, it is at position 15.
Disc #2 has 3 positions; at time=0, it is at position 2.
Disc #3 has 19 positions; at time=0, it is at position 4.
Disc #4 has 13 positions; at time=0, it is at position 2.
Disc #5 has 7 positions; at time=0, it is at position 2.
Disc #6 has 5 positions; at time=0, it is at position 0."""


def parse_input(input_str):
    lines = input_str.split("\n")
    disks = []
    for line in lines:
        line = line.strip(".")
        print(line)
        words = line.split(" ")
        bits = [int(words[3]), int(words[-1])]
        disks.append(bits)
    return disks


def valid(disks):
    no_disks = len(disks)
    result = True
    for i in range(no_disks):
        if ((disks[i][1] + 1 + i) % disks[i][0]) != 0:
            result = False
            break
    return result


def increment(disks):
    no_disks = len(disks)
    for i in range(no_disks):
        disks[i][1] = (disks[i][1] + 1) % disks[i][0]
    return disks


def day15():
    disks = parse_input(input_str)
    result = valid(disks)
    i = 0
    while not result:
        disks = increment(disks)
        result = valid(disks)
        i += 1
    return i


def day15b():
    disks = parse_input(input_str)
    disks.append([11, 0])
    print(disks)
    result = valid(disks)
    i = 0
    while not result:
        disks = increment(disks)
        result = valid(disks)
        i += 1
    return i

if __name__ == "__main__":
    #print(day15())
    print(day15b())
