
def long(strs):
    if len(strs) == 0:
        return ""
    elif len(strs)==1:
        return strs[0]
    m = min([len(x) for x in strs])
    if m == 0:
        return ""
    for x in range(m):
        for y in range(1, len(strs)):
            if strs[y][x] != strs[y - 1][x]:
                return strs[y][:x+1]

str=['a','a','a']
print(long(str))
