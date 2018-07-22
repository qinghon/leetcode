



def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    l = len(str(x))
    for i, v in enumerate(str(x)):
        if v != str(x)[l - i - 1]:
            return False
        elif i >= round(l / 2, 0):
            return True
        else:
            pass


x=1000021
print(isPalindrome(x))