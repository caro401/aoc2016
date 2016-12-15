def assemble(filename):
    regs = {"a": 0, "b": 0, "c": 1, "d": 0} 
    with open(filename) as fin:
        lines = fin.readlines()
    stuff = []
    for line in lines:
        line = line.strip("\n")
        line = line.split(" ")
        stuff.append(line)
    idx = 0
    while idx < len(lines):
        bits = stuff[idx]
        if bits[0].startswith("c"):  # copy
            if bits[1].isnumeric():
                regs[bits[2]] = int(bits[1])
            else:
                regs[bits[2]] = regs[bits[1]]
            idx +=1
            
        elif bits[0].startswith("i"):  # increase
            regs[bits[1]] += 1
            idx += 1
            
        elif bits[0].startswith("d"):  # decrease
            regs[bits[1]] -= 1
            idx += 1
            
        else: # jnz
            if bits[1].isnumeric():  # number
                if int(bits[1]) != 0:
                    idx += int(bits[2])
                else:
                    idx += 1
            else:  # contents of register
                if regs[bits[1]] != 0:
                    idx += int(bits[2])
                else:
                    idx += 1
    return regs

if __name__ == "__main__":
    print(assemble("day12test.txt"))
    print(assemble("day12in.txt"))
