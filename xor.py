"""import mod for string size of random bytes"""
from os import urandom

def gkey(length: int) -> bytes:
    """make key"""
    return urandom(length)

def xor_strings(s, t) -> bytes:
    """concat xor strings"""
    if isinstance(s, str):
        return "".join(chr(ord(a) ^ b) for a, b in zip(s, t)).encode('utf8')
    return bytes([a ^ b for a, b in zip(s, t)])

MESSAGE = 'test'
print('message:', MESSAGE)

key = gkey(len(MESSAGE))
print('key:', key)

CIPHER = xor_strings(MESSAGE.encode('utf8'), key)
print('cipher:', CIPHER)
print('decrypted:', xor_strings(CIPHER, key).decode('utf8'))

if xor_strings(CIPHER, key).decode('utf8') == MESSAGE:
    print('true')
else:
    print('false')
