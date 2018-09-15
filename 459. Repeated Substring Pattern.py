def repeatedSubstringPattern(s):
    """
    :type s: str
    :rtype: bool
    """
    temp={}
    for x in s:
        temp[x]=0
    
    for k in temp.keys():
        temp[k]=s.count(k)
    print(temp)
    if max(list(temp.values()))!=min(list(temp.values())):
        return False
    else:
        return True

s='abababababababc'
print(repeatedSubstringPattern(s))
