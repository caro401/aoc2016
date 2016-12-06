from collections import defaultdict

def decode(filename, mode):
    
    with open(filename) as fin:
        lines = fin.readlines()
    length = len(lines[0]) - 1
    counts = [defaultdict(int) for i in range(length)] 
    for line in lines:
        line = line.strip("\n")
        for i in range(length):
            counts[i][line[i]] += 1
    for i in range(length):
        if mode == "max":
            print(max(counts[i].keys(), key=lambda key: counts[i][key]), end="")
        else: # mode = min
            print(min(counts[i].keys(), key=lambda key: counts[i][key]), end="")

    print("\n")
        
if __name__ == "__main__":
    decode("day6test.txt", "max")
    decode("day6in.txt", "max")
    decode("day6test.txt", "min")
    decode("day6in.txt", "min")
        