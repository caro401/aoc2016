from hashlib import md5
import re


def pad(salt):
    pattern3 = re.compile(r"(.)\1\1")
    pattern5 = re.compile(r"(.)\1\1\1\1")
    digit = 0
    keys = []
    while len(keys) < 64:
        hash_str = md5(bytes(salt + str(digit), 'utf-8')).hexdigest()
        triples = re.search(pattern3, hash_str)
        if triples:
            repeat_char = triples.group(0)[0]
            for i in range(1, 1000):
                new_hash = md5(bytes(salt + str(digit+i), 'utf-8')).hexdigest()
                fives = re.search(pattern5, new_hash)
                if fives and (fives.group(0)[0] == repeat_char):
                    keys.append((new_hash, digit))
                    break
        digit += 1
    return keys[-1]


def secure_pad(salt):
    pattern3 = re.compile(r"(.)\1\1")
    pattern5 = re.compile(r"(.)\1\1\1\1")
    digit = 0
    keys = []
    while len(keys) < 64:
        hash_str = md5(bytes(salt + str(digit), 'utf-8')).hexdigest()
        for i in range(2016):
            hash_str = md5(bytes(hash_str, 'utf-8')).hexdigest()
        triples = re.search(pattern3, hash_str)
        if triples:
            repeat_char = triples.group(0)[0]
            for i in range(1, 1000):
                new_hash = md5(bytes(salt + str(digit+i), 'utf-8')).hexdigest()
                for j in range(2016):
                    new_hash = md5(bytes(new_hash, 'utf-8')).hexdigest()
                fives = re.search(pattern5, new_hash)
                if fives and (fives.group(0)[0] == repeat_char):
                    keys.append((new_hash, digit))
                    break
        digit += 1
    return keys[-1]


if __name__ == "__main__":
    print(secure_pad("cuanljph"))
