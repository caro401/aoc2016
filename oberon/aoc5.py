import hashlib
input = "ffykfhsq"

def md5(s):
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()

def five_oh(s):
    i = 0
    while True:
        hsh = md5("%s%d"%(s,i))
        if hsh.startswith("00000"):
            yield hsh[5:7]
        i+=1

gn = five_oh(input)

#print "".join([gn.next()[0] for i in range(8)])

pw = ["."]*8

ifound = 0
while ifound < 8:
    hx = gn.next()
    print hx
    if hx[0] in "01234567":
        if pw[int(hx[0])] == ".":
            ifound += 1
            pw[int(hx[0])] = hx[1]
            print "".join(pw)
            
print "".join(pw)
    
