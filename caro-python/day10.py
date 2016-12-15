def pass_chips(filename):
    bots = [list() for x in range(210)]  # guess at how many bots and outputs
    outputs = [list() for x in range(25)]
    instructions = [list() for x in range(210)]
    
    # preprocessing, get what the bots start with and their instructions
    with open(filename) as fin:
        for line in fin:
            line = line.strip("\n")
            if line.startswith("v"):  # value x goes to bot y
                nums = [int(x) for x in line.split(" ") if x.isnumeric()]  # array [value, bot]
                bots[nums[1]].append(nums[0])
            else: # bot x gives low to bot/output y and high to bot/output z
                line = line.split(" ")
                nums = [int(x) for x in line if x.isnumeric()]
                instructions[nums[0]] = [line[5][0], nums[1], line[10][0], nums[2]]
                # ["o", 2, "b", 4] low to out 2, high to bot 4
                
    # process the bots            
    nextBot = [i for i in bots if len(i) == 2]  # the one with 2 things
    while nextBot:
        currentBot = bots.index(nextBot[0])
        if (17 in bots[currentBot]) & (61 in bots[currentBot]):
            print("found the bot", currentBot)
        low, high = min(bots[currentBot]), max(bots[currentBot])
        bots[currentBot] = list()
        do = instructions[currentBot]
        if do[0] == "o":
            outputs[do[1]].append(low)
        else:
            bots[do[1]].append(low)
        if do[2] == "o":
            outputs[do[3]].append(high)
        else:
            bots[do[3]].append(high)
        nextBot = [i for i in bots if len(i) == 2]
    print("outputs", outputs[0][0] * outputs[1][0] * outputs[2][0])
            
if __name__ == "__main__":
    pass_chips("day10test.txt")
    pass_chips("day10in.txt")