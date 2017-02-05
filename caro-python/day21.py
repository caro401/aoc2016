from itertools import permutations

def mv(line, data):
    nums = [int(x) for x in line.split(" ") if x.isnumeric()]
    move_char = data.pop(nums[0])
    data.insert(nums[1], move_char)
    return data


def rev(line, data):
    nums = [int(x) for x in line.split(" ") if x.isnumeric()]
    rev_chunk = data[nums[0]: nums[1]+1]
    rev_chunk.reverse()
    new_data = []
    new_data.extend(data[:nums[0]])
    new_data.extend(rev_chunk)
    new_data.extend(data[nums[1]+1:])
    return new_data


def swap_pos(line, data):
    return swap([int(x) for x in line.split(" ") if x.isnumeric()], data)


def swap_letter(line, data):
    line = line.split(" ")
    return swap([data.index(line[2]), data.index(line[-1])], data)


def swap(nums, data):
    data[nums[0]], data[nums[1]] = data[nums[1]], data[nums[0]]
    return data


def rotate_l(line, data):
    line = line.split(" ")
    return shift(data, int(line[2]))


def rotate_r(line, data):
    line = line.split(" ")
    return shift(data, -1 * int(line[2]))


def rotate_base(line, data):
    line = line.split(" ")
    n = data.index(line[-1])
    steps = 1 + n
    if n >= 4:
        steps += 1
    return shift(data, -1 * steps)


def shift(data, n):
    n %= len(data)
    return data[n:] + data[:n]

FUNC_DICT = {
    "move pos": mv,
    "reverse ": rev,
    "swap pos": swap_pos,
    "swap let": swap_letter,
    "rotate b": rotate_base,
    "rotate l": rotate_l,
    "rotate r": rotate_r
}


def day21(filename, input_str):
    data = list(input_str)
    with open(filename) as fin:
        for line in fin:
            line = line.strip("\n")
            data = FUNC_DICT[line[:8]](line, data)
    return "".join(data)


def day21b(filename):
    combos = permutations("abcdefgh")
    for c in combos:
        data = list(c)
        with open(filename) as fin:
            for line in fin:
                line = line.strip("\n")
                data = FUNC_DICT[line[:8]](line, data)
                if "".join(data) == "fbgdceah":
                    if day21(filename, c) == "fbgdceah":
                        return "".join(c)


if __name__ == "__main__":
    print(day21("day21.txt", "abcdefgh"))
    print(day21b("day21.txt"))
