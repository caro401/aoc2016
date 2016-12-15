def triangles(filename):
    count = 0
    with open(filename) as fin:
        for line in fin:
            numbers = clean(line)
            if isTriangle(numbers[0], numbers[1], numbers[2]):
                count += 1
    return count
    
def columns(filename):
    count = 0
    x= []
    with open(filename) as fin:
        lines = fin.readlines()
    for line in lines:
        numbers = clean(line)
        x.append(numbers)
    i = 0 
    numLines = len(x)
    while i < numLines -2:
        for j in range(3):
            if isTriangle(x[i][j], x[i+1][j], x[i+2][j]):
                count += 1
        i += 3
    return count
    
def clean(line):
    numbers = line.split("  ")
    while "" in numbers: 
        numbers.remove("")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i].strip("\n"))
    return numbers
    
def isTriangle(num1, num2, num3):
    return (num1 + num2 > num3) & (num2 + num3 > num1) & (num3 + num1 > num2)
    
if __name__ == "__main__":
    print(triangles("day3test.txt"))
    print(triangles("day3in.txt"))
    print(columns("day3test.txt"))
    print(columns("day3in.txt"))
            