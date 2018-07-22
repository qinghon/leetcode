def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    num = {}
    for i, v in enumerate(s):
        if v not in num:
            num[v] = 1
        else:
            num[v] += 1
    temp = {value: key for key, value in num.items()}
    values_list = temp.values
    values_list.sort(reverse=True)
    r_str = ''
    for v in values_list:
        r_str += temp[v] * int(v)
    return r_str

print(frequencySort('tree'))