
def checkPerfectNumber(num):
    k = num.bit_length() // 2
    return num > 1 and num == ((2 << k) - 1) << k
print(checkPerfectNumber(32640))