
def isAnagram(s,t):
    if len(s ) !=len(t) or set(s ) !=set(t):
        return False
    a= {}
    b = {}
    for sx, tx in zip(s, t):
        if not a.__contains__(sx):
            a[sx] = 1
        else:
            a[sx] += 1
        if not b.__contains__(tx):
            b[tx] = 1
        else:
            b[tx] += 1
    if a == b:
        return True
    else:
        return False

s="anagram"
t="nagaram"



print(isAnagram(s,t))