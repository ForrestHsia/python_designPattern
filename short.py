ALPHABET = base62String()
def base62_encode(num, alphabet=ALPHABET):
    """10進制轉62進制"""
    if (num == 0):
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    return ''.join(arr[::-1])

# 產生62位字元
def base62String():
    alphabet = ""
    for i in range(48,58):
        alphabet += chr(i)
    for i in range(65, 91):
        alphabet += chr(i)
    for i in range(97, 123):
        alphabet += chr(i)  
    return alphabet
a = base62String()
print(a)