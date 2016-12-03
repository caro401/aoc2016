def walk(path):
    location = [0, 0]
    direction = 0
    steps = path.split(",")
    for step in steps:
        step = step.strip(" ")
        distance = int(step[1:])
        if step[0] == "L":
            direction = (direction -1) %4
        else:
            direction = (direction + 1) % 4
        
        location = move(distance, direction, location)
    return abs(location[0]) + abs(location[1])
    
def revisit(path):
    location = [0, 0]
    visited = [tuple(location)]
    direction = 0
    steps = path.split(",")
    for step in steps:
        step = step.strip(" ")
        distance = int(step[1:])
        if step[0] == "L":
            direction = (direction -1) %4
        else:
            direction = (direction + 1) % 4
        
        moved = 1
        while moved <= distance:
            location = move2(1, direction, location)
            if tuple(location) not in visited:
                visited.append(tuple(location))
            else:
                return abs(location[0]) + abs(location[1])
            moved += 1

def move(distance, direction, location):
    # direction 0 = facing north, 1 = facing east 2 = facing south 3 = facing west
    if direction == 0:  # facing north
        location[0] += distance  # move east (or west)
    elif direction == 1:
        location[1] -= distance
    elif direction == 2:
        location[0] -= distance
    elif direction == 3:
        location[1] += distance
    else:
        print("you messed up maths")
    return location
    

def move2(distance, direction, location):
    if direction == 1: #east
        location[0] += distance
    elif direction == 2: #south
        location[1] -= distance
    elif direction == 3: #west
        location[0] -= distance
    else:
        location[1] += distance
    return location



if __name__ == "__main__":
    print(walk("R2, L3"))
    print(walk("R2, R2, R2"))
    print(walk("R5, L5, R5, R3"))
    path ="R4, R4, L1, R3, L5, R2, R5, R1, L4, R3, L5, R2, L3, L4, L3, R1,\
    R5, R1, L3, L1, R3, L1, R2, R2, L2, R5, L3, L4, R4, R4, R2, L4, L1, R5, L1,\
    L4, R4, L1, R1, L2, R5, L2, L3, R2, R1, L194, R2, L4, R49, R1, R3, L5, L4, \
    L1, R4, R2, R1, L5, R3, L5, L4, R4, R4, L2, L3, R78, L5, R4, R191, R4, R3, \
    R1, L2, R1, R3, L1, R3, R4, R2, L2, R1, R4, L5, R2, L2, L4, L2, R1, R2, L3,\
    R5, R2, L3, L3, R3, L1, L1, R5, L4, L4, L2, R5, R1, R4, L3, L5, L4, R5, L4,\
    R5, R4, L3, L2, L5, R4, R3, L3, R1, L5, R5, R1, L3, R2, L5, R5, L3, R1, R4,\
    L5, R4, R2, R3, L4, L5, R3, R4, L5, L5, R4, L4, L4, R1, R5, R3, L1, L4, L3,\
    L4, R1, L5, L1, R2, R2, R4, R4, L5, R4, R1, L1, L1, L3, L5, L2, R4, L3, L5,\
    L4, L1, R3"
    print(walk(path))
    print(revisit("R8, R4, R4, R8"))
    print(revisit(path))
