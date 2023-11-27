from os import urandom

def gkey(length: int) -> bytes:
    # generate key
    return urandom(length)

def xor_strings(s, t) -> bytes:
    # concatenate xor strings
    if isinstance(s, str):
        return "".join(chr(ord(a) ^ b) for a, b in zip(s, t)).encode("utf8")
    return bytes([a ^ b for a, b in zip(s, t)])

MESSAGE = "I'm bored as hell"
key = gkey(len(MESSAGE))
CIPHER = xor_strings(MESSAGE.encode("utf8"), key)

print("message:", MESSAGE)
print("key:", key)
print("cipher:", CIPHER)
print("decrypted:", xor_strings(CIPHER, key).decode("utf8"))

# check
# if xor_strings(CIPHER, key).decode('utf8') == MESSAGE:
    # print("true")
# else:
    # print("false")
