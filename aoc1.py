import re

inp = "R4, R4, L1, R3, L5, R2, R5, R1, L4, R3, L5, R2, L3, L4, L3, R1, R5, R1, L3, L1, R3, L1, R2, R2, L2, R5, L3, L4, R4, R4, R2, L4, L1, R5, L1, L4, R4, L1, R1, L2, R5, L2, L3, R2, R1, L194, R2, L4, R49, R1, R3, L5, L4, L1, R4, R2, R1, L5, R3, L5, L4, R4, R4, L2, L3, R78, L5, R4, R191, R4, R3, R1, L2, R1, R3, L1, R3, R4, R2, L2, R1, R4, L5, R2, L2, L4, L2, R1, R2, L3, R5, R2, L3, L3, R3, L1, L1, R5, L4, L4, L2, R5, R1, R4, L3, L5, L4, R5, L4, R5, R4, L3, L2, L5, R4, R3, L3, R1, L5, R5, R1, L3, R2, L5, R5, L3, R1, R4, L5, R4, R2, R3, L4, L5, R3, R4, L5, L5, R4, L4, L4, R1, R5, R3, L1, L4, L3, L4, R1, L5, L1, R2, R2, R4, R4, L5, R4, R1, L1, L1, L3, L5, L2, R4, L3, L5, L4, L1, R3"

EAST, SOUTH, WEST, NORTH = range(4)

DIRS = [(1,0),(0,-1),(-1,0),(0,1)]

d = NORTH

c = [0,0]
s = set()
s.add((0,0))
for t in inp.split(","):
    if "L" in t:
        d -= 1
    elif "R" in t:
        d += 1
    else:
        raise "broken"
    d = d%4
    
    n = re.search("([0-9]+)", t)
    if n is not None:
        nn = int(n.group(0))
        for j in range(nn):
            c[0] += DIRS[d][0]
            c[1] += DIRS[d][1]
            if tuple(c) in s:
                print abs(c[0])+abs(c[1])
                break
            else:
                s.add(tuple(c))
    else:
        raise "broken"


    
