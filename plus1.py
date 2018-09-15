def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    k = len(digits) - 1
    if digits[k] != 9:
        digits[k] += 1
        return digits

    def plus1(digits, k):

        if digits[k] == 9:
            if k > 0:
                digits[k] = 0
                digits=plus1(digits, k - 1)
            else:
                digits[k] = 0
                digits = [1] + digits
                return digits

        else:
            digits[k] += 1

        return digits

    return plus1(digits, k)


a = [9, 9]

print(plusOne(a))
