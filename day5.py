from hashlib import md5

def code(doorId):
    number = 0
    password = ""
    for i in range(8):
        newchar, number = getInterestingHash(doorId, number)
        password += newchar
        print(newchar)
    return password
    
    
def getInterestingHash(doorId, number):
    hashVal = ""
    while not hashVal.startswith('00000'):
        number += 1
        hashVal = md5(bytes(doorId + str(number), 'utf-8')).hexdigest()
    return hashVal[5], number
    
    
def code2(doorId):
    number = 0
    password = ["_"] * 8
    while "_" in password:
        newchar, number, position = getCinemaHash(doorId, number)
        if position < 8:
            if password[position] == "_":
                password[position] = newchar
        print(password)  # so you know it is actually doing something 
    return password
    
def getCinemaHash(doorId, number):
    hashVal = ""
    while not hashVal.startswith('00000'):
        number += 1
        hashVal = md5(bytes(doorId + str(number), 'utf-8')).hexdigest()
        position = hashVal[5]
        if position.isdigit():
            position = int(position)
        else:
            position = 8 # can't convert to int, so pick a random invalid position
    return hashVal[6], number, position
    

if __name__ == "__main__":
    print(code("abc"))
    print(code("wtnhxymk")
    print(code2("abc"))
    print(code2("wtnhxymk"))