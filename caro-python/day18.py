inp = ".^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^"
test = ".^^.^.^^^^"


def gen_next_row(curr_row):
    """A new tile is a trap iff:
        Its left and center tiles are traps, but its right tile is not.
        Its center and right tiles are traps, but its left tile is not.
        Only its left tile is a trap.
        Only its right tile is a trap."""
    curr_row = "." + curr_row + "."
    next_row = ""
    trap_strings = ["^^.", ".^^", "^..", "..^"]
    for i in range(1, len(curr_row)-1):
        if curr_row[i-1:i+2] in trap_strings:
            next_row += "^"
        else:
            next_row += "."
    return next_row


def count_safe(row):
    total = 0
    for c in row:
        if c == ".":
            total += 1
    return total


def day18(input_str, rows):
    current = input_str
    safe = count_safe(current)
    for i in range(rows-1):
        current = gen_next_row(current)
        safe += count_safe(current)
    return safe


if __name__ == "__main__":
    print(day18(inp, 40))
    print(day18(inp, 400000))
