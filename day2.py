import numpy

def findCode(instructionsFilename):
    with open(instructionsFilename) as fin:
        instructions = fin.readlines()
    keypad = numpy.arange(1,10).reshape(3,3)
    position = [1,1]
    
    for line in instructions:
        for c in line.strip("\n"):
            if c == "U":
                if position[0] > 0:
                    position[0] -= 1
            elif c == "D":
                if position[0] < 2:
                    position[0] += 1
            elif c == "L":
                if position[1] > 0:
                    position[1] -= 1
            elif c == "R":
                if position[1] < 2:
                    position[1] += 1
            
            else:
                print("bad char!")
                
        print(keypad[position[0], position[1]])
        
        
        
def findCode2(instructionsFilename):
    with open(instructionsFilename) as fin:
        instructions = fin.readlines()
    keypad = numpy.array(  [[0,0,1,0,0],
                [0,2,3,4,0],
                [5,6,7,8,9],
                [0, "A", "B", "C", 0],
                [0, 0, "D", 0, 0]])
    position = [3, 0]
    for line in instructions:
        for c in line.strip("\n"):
            if c == "U":
                if (position[0] > 0): 
                    if (keypad[position[0]-1, position[1]] != "0"):
                        position[0] -= 1
            elif c == "D":
                if (position[0] < 4):  # dont move if that will take you off the bottom of the array
                    if keypad[position[0] + 1, position[1]] != "0":
                        position[0] += 1
            elif c == "L":
                if (position[1] > 0):
                    if (keypad[position[0], position[1] - 1] != "0"):
                        position[1] -= 1
            elif c == "R":
                if (position[1] < 4):
                    if keypad[position[0], position[1] + 1] != "0":
                        position[1] += 1
            
            else:
                print("bad char!")
        print("code: ", keypad[position[0], position[1]])
        
        
        
if __name__ == "__main__":
    #findCode("day2test.txt")
    #findCode("day2in.txt")
    print("\n")
    #findCode2("day2test.txt")
    findCode2("day2in.txt")