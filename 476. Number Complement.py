def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    l = 0
    for x in range(32):
        if num >= 2 ** x and num <= 2 ** (x+1):
            l = 2**(x+1)-1

    f_num = num ^ (l)
    return f_num
print(findComplement(1))