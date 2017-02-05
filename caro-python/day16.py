input_str = "11101000110010100"


def fill_disk(data):
    """Call the data you have at this point "a".
        Make a copy of "a"; call this copy "b".
        Reverse the order of the characters in "b".
        In "b", replace all instances of 0 with 1 and all 1s with 0.
        The resulting data is "a", then a single 0, then "b"."""
    new_str = ""
    stuff = "".join(reversed(data))
    for char in stuff:
        if char == "0":
            new_str += "1"
        else:
            new_str += "0"
    return data + "0" + new_str


def checksum(data):
    num = int(len(data)/2)
    ans = ""
    for i in range(num):
        if data[2*i] == data[2*i+1]:
            ans += "1"
        else:
            ans += "0"
    if (len(ans) % 2) == 0:
        return checksum(ans)
    return ans


def day16(data, disk_len):
    while len(data) < disk_len:
        data = fill_disk(data)
    data = data[:disk_len]
    return checksum(data)

if __name__ == "__main__":
    print(day16(input_str, 272))
    print(day16(input_str, 35651584))
