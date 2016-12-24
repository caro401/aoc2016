from hashlib import md5


def code(door_id):
    number = 0
    password = ""
    for i in range(8):
        newchar, number = get_interesting_hash(door_id, number)
        password += newchar
        print(newchar)
    return password
    
    
def get_interesting_hash(door_id, number):
    hash_val = ""
    while not hash_val.startswith('00000'):
        number += 1
        hash_val = md5(bytes(door_id + str(number), 'utf-8')).hexdigest()
    return hash_val[5], number
    
    
def code2(door_id):
    number = 0
    password = ["_"] * 8
    while "_" in password:
        newchar, number, position = get_cinema_hash(door_id, number)
        if position < 8:
            if password[position] == "_":
                password[position] = newchar
        print(password)  # so you know it is actually doing something 
    return password


def get_cinema_hash(door_id, number):
    hash_val = ""
    while not hash_val.startswith('00000'):
        number += 1
        hash_val = md5(bytes(door_id + str(number), 'utf-8')).hexdigest()
        position = hash_val[5]
        if position.isdigit():
            position = int(position)
        else:
            position = 8  # can't convert to int, so pick a random invalid position
    return hash_val[6], number, position
    

if __name__ == "__main__":
    print(code("abc"))
    print(code("wtnhxymk"))
    print(code2("abc"))
    print(code2("wtnhxymk"))
