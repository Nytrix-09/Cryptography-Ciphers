class VignereCipher:

    def __init__ (self):
        self.plain_text=""
    
    def start_encrypt_decrypt(self):
        choice=int(input("Enter 1 for Encrytion and 0 for Decryption: "))
        if(choice==1):
            self.vigEncrypt()
        elif(choice==0):
            self.vigDecrypt()
        else:
            print("Please enter either 1 or 0..")
        
    def vigEncrypt(self):
        plain_text=input("Enter Plain Text: ")
        key=input("Enter key for Encryption: ")

        if(len(plain_text)==len(key)):
            key=key
        
        else:
            for i in range(len(plain_text)-len(key)):
                key+=key[i % len(key)]
        
        cipher_txt=""
        for i in range(len(plain_text)):
            if(ord(plain_text[i])>=65 and ord(plain_text[i])<92):
                cipher_txt+=chr((ord(plain_text[i])+ord(key[i]))%26+65)
            
            elif(ord(plain_text[i])>=97 and ord(plain_text[i])<123):
                cipher_txt+=chr((ord(plain_text[i])+ord(key[i]))%26+97)
            
            else:
                cipher_txt+=plain_text[i]
        print("Encrypted Text: " + cipher_txt)
    
    def vigDecrypt(self):
        cipher_message=input("Enter Cipher Text: ")
        key2=input("Enter key for Decryption: ")

        if(len(cipher_message)==len(key2)):
            key2=key2
        
        else:
            for i in range(len(cipher_message)-len(key2)):
                key2+=key2[i % len(key2)]
        
        original_txt=""
        for i in range(len(cipher_message)):
            if(ord(cipher_message[i])>=65 and ord(cipher_message[i])<92):
                if((ord(cipher_message[i])-ord(key2[i]))<0):
                    original_txt+=chr((((ord(cipher_message[i])-ord(key2[i]))+26)%26)+65)
                else:
                    original_txt+=chr(((ord(cipher_message[i])-ord(key2[i]))%26)+65)
            
            elif(ord(cipher_message[i])>=97 and ord(cipher_message[i])<123):
                if((ord(cipher_message[i])-ord(key2[i]))<0):
                    original_txt+=chr((((ord(cipher_message[i])-ord(key2[i]))+26)%26)+97)
                else:
                    original_txt+=chr(((ord(cipher_message[i])-ord(key2[i]))%26)+97)
            
            else:
                original_txt+=cipher_message[i]
        print("Original Text: " + original_txt)

if __name__ == "__main__":
    vc=VignereCipher()
    vc.start_encrypt_decrypt()

            
