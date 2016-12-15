import re
import regex

def tls(filename):
    count = 0
    with open(filename) as fin:
        for line in fin:
            inBrackets, outBrackets = unbracket(line)
            inValid = True
            outValid = False
            for chunk in inBrackets:
                if abba(chunk):
                    inValid = False
            for chunk in outBrackets:
                if abba(chunk):
                    outValid = True
            if inValid & outValid:
                count += 1
    return count
    
def ssl(filename):
    count = 0
    with open(filename) as fin:
        for line in fin:
            valid = False
            inBrackets, outBrackets = unbracket(line)
            abas = set()
            for item in outBrackets:
                new = bab(item)
                if new:
                    abas.update(new)
            babs = set()
            for item in inBrackets:
                new = bab(item)
                if new:
                    babs.update(new)
            for item in babs:  
                if item[1] != item[0]:
                    aba = item[1] + item[0] + item[1]
                    if aba in abas:
                        valid = True
            if valid:
                count += 1
    return count
            
def unbracket(line):
    inBrackets = re.findall(r"\[([a-z]+)\]", line)
    outBrackets = re.findall(r"\]([a-z]+)\[", line)
    outBrackets.append(line[:line.find("[")]) # the first bit
    outBrackets.append(line[line.rfind("]")+1:-1])  # the last bit
    return inBrackets, outBrackets

def abba(word):
    result = re.search(r"(.)(.)\2\1", word) 
    if not result:
        return False
    else: 
        return not(word[result.start()] == word[result.start() + 1])

def bab(word):
    babs = regex.findall(r"((.)(.)\2)", word, overlapped=True)  # NEAT!
    if not babs:
        return False
    return [item[0] for item in babs]
        
if __name__ == "__main__":
    print(tls("day7test.txt"))
    print(tls("day7in.txt"))
    print(ssl("day7test.txt"))
    print(ssl("day7in.txt"))