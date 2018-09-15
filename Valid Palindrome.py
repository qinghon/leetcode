

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    abc = 'asdfghjklqwertyuiopzxcvbnm'
    t=''
    t=t+x for x in s.lower() if x in abc

    return t[::-1] == t

st="A man, a plan, a canal: Panama"

print(isPalindrome(st))
