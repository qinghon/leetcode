
def long(strs):
    if len(strs) == 0:
        return ""
    m = min([len(x) for x in strs])
    if m == 0:
        return ""
    for x in range(m):
        c=strs[0][x]
        if not all([strd[x] ==c for strd in strs]):
                return strs[0][0:x]
        else:
            if x==m-1:
                return strs[0][0:x+1]
    return strs[0]



str=["flower","flow","flight"]
print(long(str))
