def encode_caesar(message, shift):
    result = ''
    base = 0
    for i in message:
        if i.isalpha():
            if i.isupper():
                base = ord('A')
            else:
                base = ord('a')
            shifted = (ord(i) - base + shift)%26 + base
            result += chr(shifted)
        else:
            result += i
    return result

def decode_caesar(message, shift):
    result = ''
    base = 0
    for i in message:
        if i.isalpha():
            if i.isupper():
                base = ord('A')
            else:
                base = ord('a')
            shifted = (ord(i) - base - shift)%26 + base
            result += chr(shifted)
        else:
            result += i
    return result

original = 'Hello world'
encoded_msg = encode_caesar(original, 4)
decoded_msg = decode_caesar(encoded_msg, 4)

print(original, encoded_msg, decoded_msg)
        




