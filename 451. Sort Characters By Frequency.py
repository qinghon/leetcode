def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    num = {}
    r_str=''
    for i, v in enumerate(s):
        if v not in num:
            num[v] = 1
        else:
            num[v] += 1

    T_v_list=sorted(num.items(),key=lambda item:item[1],reverse=True)

    for k,v in T_v_list:
        r_str+=k*v


    return r_str

print(frequencySort('treessstdfasd'))
