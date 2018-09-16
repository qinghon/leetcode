def findNthDigit(n):
    """
    :type n: int
    :rtype: int
    """
    legth=9
    count=1
    temp=9
    ln=1
    while n>legth:
        n -= temp * count
        count+=1
        ln *= 10
        temp *= 10
        legth+=(temp*count)
    res=int(str((n-1)//count+ln)[(n-1)%count])
    return res

print(findNthDigit(10000))
