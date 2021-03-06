def caesar(data, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÔÕÍÚÇ '
    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data

# Tests
key = 5
original = 'hello world'
print('\n   Original:', original)
ciphered = caesar(original, key, MODE_ENCRYPT)
print('\n Encriptada:', ciphered)
plain = caesar(ciphered, key, MODE_DECRYPT)
print('\n Decriptada:', plain)
print('\n chave usada:', key)
print('\n')

