class VernamCipher:

    def __init__(self):
        self.user_input=""
    
    def start_encrypt_decrypt(self):
        choice=int(input("Enter 1 for Encryption and 0 for Decryption: "))
        if(choice==1):
            self.vernamEnc()
        elif(choice==0):
            self.vernamDec()
        else:
            print("Enter Valid Choice!!")
        
    
    def vernamEnc(self):
        cipher_txt=""
        plain_text=input("Enter plain text for Encryption: ")
        pt=plain_text.upper()
        key = input("Enter key for Encryption: ")
        kt=key.upper()
        if(len(key)!=len(plain_text)):
            print("Length of key does not match length of Plain Text!")
        
        else:
            for i in range (len(plain_text)): 
                if (pt[i]==' '):
                    cipher_txt+=' '
                else:
                    cipher_txt+=chr(((ord(pt[i]) + ord(kt[i]))%65)+65) 
            
        print("Cipher Text: "+ cipher_txt)


    def vernamDec(self):
        original_txt=""
        coded_text=input("Enter cipher text for Decryption: ")
        ct=coded_text.upper()
        key2 = input("Enter key for Decryption: ")
        kt2=key2.upper()
        if(len(key2)!=len(coded_text)):
            print("Length of key does not match length of cipher Text!")
        
        else:
            for i in range (len(coded_text)) :
                if (ct[i]==' '):
                    original_txt+=' '
                else:
                    original_txt+=chr(((ord(ct[i]) - ord(kt2[i]))%65)+65) 
            
        print("Original Text: " + original_txt)
    

if __name__ == "__main__":
    vc=VernamCipher()
    vc.start_encrypt_decrypt()

    
