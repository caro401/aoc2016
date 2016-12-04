from collections import Counter

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def checkRoom(filename):
    total = 0
    with open(filename) as fin:
        for line in fin:
            counts, sector, checksum = parse(line)
            common = mostCommon(counts)
            real = True
            for letter in common:
                if letter not in checksum:
                    real = False
            if real:
                total += int(sector)
                decrypt(line)  # for part 2 only, just prints all the valid lines to the console
    return total 
            
def parse(line):
    parts = line.split("[")
    checksum = parts[1].strip("]\n")
    sector = parts[0][-3:]
    letters = parts[0][:-3]
    letters = [c for c in letters if c.isalpha()]
    counts = Counter(letters)
    return counts, sector, checksum

def decrypt(line):
    parts = line.split("[")
    sector = int(parts[0][-3:])
    letters = list(parts[0][:-3].replace("-", " ")) # slice off sector id, replace - with space
    for i in range(len(letters)):
        if letters[i].isalpha():
            index = ALPHABET.index(letters[i])
            letters[i] = ALPHABET[(index + sector) % 26]
    print("".join(letters), sector)

def mostCommon(countsDict):
    common = [v[0] for v in sorted(countsDict.items(), key=lambda kv: (-kv[1], kv[0]))]
    return common[:5]
    
    
if __name__ == "__main__":
    print(checkRoom("day4test.txt"))
    print(checkRoom("day4in.txt"))
    print(decrypt("qzmt-zixmtkozy-ivhz-343[absce]"))
    