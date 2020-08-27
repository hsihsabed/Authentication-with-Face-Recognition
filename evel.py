def evel(s):
    val = 0
    for i in range(len(s)):
        x = ord(s[i])
        val += (10**(i+1))*(x**(len(s)-i))
    return hex(val)


