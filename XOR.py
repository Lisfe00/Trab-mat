def repeated_key_xor(plain_text, key): 
    
    
    pt = plain_text 
    len_key = len(key) 
    encoded = [] 
      
    for i in range(0, len(pt)): 
        encoded.append(pt[i] ^ key[i % len_key]) 
    return bytes(encoded) 
def main(): 
    plain_text = b'Hello World!!'
    key = b'ICE'
      
    print("Plain text: ", plain_text) 
    print("Encrypted as: ", repeated_key_xor(plain_text, key).hex()) 
  
if __name__ == '__main__': 
    main() 