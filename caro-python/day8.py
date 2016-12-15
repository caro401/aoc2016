import numpy as np

def decode(filename):
    np.set_printoptions(linewidth=150)
    pad = np.zeros((6,50), dtype=np.int)
    with open(filename) as fin:
        for line in fin:
            if line.startswith("re"):  # rect
                nums = line[line.find(" "):].split("x")
                pad[0:int(nums[1]), 0:int(nums[0])] = 1
            else:
                nums = line[line.find("=")+1:].split(" ")
                if line[7] == "r":  # row
                    pad = rowRotate(pad, int(nums[0]), int(nums[2]))
                else: # column
                    pad = colRotate(pad, int(nums[0]), int(nums[2]))
    print(pad)
    return np.sum(pad)
                    
def rowRotate(pad, row, steps):
    steps = steps % 50
    moveChunk = list(pad[row,:][-1*steps:])
    pad[row,:][steps:] = pad[row,:][:-1* steps]
    pad[row,:][:steps] = moveChunk
    return pad
    
def colRotate(pad, col, steps):
    steps = steps % 6
    moveChunk = list(pad[:,col][steps *-1:])
    pad[:,col][steps:] = pad[:,col][:-1* steps]
    pad[:,col][:steps] = moveChunk
    return pad
    
if __name__ == "__main__":
    testpad = np.zeros((3,7), dtype=np.bool)
    testpad[0:2, 0:3] = True
    print(testpad, "\n\n")
    print(colRotate(testpad, 1, 1))
    print(rowRotate(testpad, 0, 4))
    print(colRotate(testpad, 1, 1), "\n\n")
    print(decode("day8in.txt"))
