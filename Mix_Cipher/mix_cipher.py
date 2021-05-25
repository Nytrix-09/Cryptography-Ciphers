class MixCipher:
    
    def __init__(self):
        self.plain_text=""

    def start_encrypt_decrypt(self):
        choice=int(input("Enter 1 for Encryption and 0 for Decryption: "))
        if (choice == 1):
            self.mixencrypt()
        elif (choice== 0):
            self.mixdecrypt()
        else:
            print("Pls Enter Valid Number!")
        
    def mixencrypt (self):
        print("Enter 3 keys for Encryption: \n")
        ek1=int(input())
        ek2=int(input())
        ek3=int(input())
        plain_text=input("Enter plain text: ")
        encrypt=""
        for i in  range(len(plain_text)):
            if(ord(plain_text[i])>=65 and ord(plain_text[i])<92):
                if(i%3==0):
                    encrypt+=chr((((ord(plain_text[i])-65)+ek1)%26)+65)
                elif (i%3==1):
                    encrypt+=chr((((ord(plain_text[i])-65)+ek2)%26)+65)
                elif(i%3==2):
                    encrypt+=chr((((ord(plain_text[i])-65)+ek3)%26)+65)
                else:
                    encrypt+=chr((((ord(plain_text[i])-65)+ek3)%26)+65)
            
            elif(ord(plain_text[i])>=97 and ord(plain_text[i])<122):
                if(i%3==0):
                    encrypt+=chr((((ord(plain_text[i])-97)+ek1)%26)+97)
                elif (i%3==1):
                    encrypt+=chr((((ord(plain_text[i])-97)+ek2)%26)+97)
                elif(i%3==2):
                    encrypt+=chr((((ord(plain_text[i])-97)+ek3)%26)+97)
                else:
                    encrypt+=chr((((ord(plain_text[i])-97)+ek3)%26)+97)
                
            else:
                encrypt+=plain_text[i]
        print("Encrypted Text: " + encrypt)
        
    def mixdecrypt (self):
        print("Enter 3 keys for decyrption: \n")
        dk1=int(input())
        dk2=int(input())
        dk3=int(input())
        plain_text=input("Enter mix text: ")
        decrypt=""

        for i in range(len(plain_text)):
            if(ord(plain_text[i])>=65 and ord(plain_text[i])<92):
                if(i%3==0):
                    decrypt+=chr((((ord(plain_text[i])-65)-dk1)%26)+65)
                elif (i%3==1):
                    decrypt+=chr((((ord(plain_text[i])-65)-dk2)%26)+65)
                elif(i%3==2):
                    decrypt+=chr((((ord(plain_text[i])-65)-dk3)%26)+65)
                else:
                    decrypt+=chr((((ord(plain_text[i])-65)-dk3)%26)+65)
            
            elif(ord(plain_text[i])>=97 and ord(plain_text[i])<122):
                if(i%3==0):
                    decrypt+=chr((((ord(plain_text[i])-97)-dk1)%26)+97)
                elif (i%3==1):
                    decrypt+=chr((((ord(plain_text[i])-97)-dk2)%26)+97)
                elif(i%3==2):
                    decrypt+=chr((((ord(plain_text[i])-97)-dk3)%26)+97)
                else:
                    decrypt+=chr((((ord(plain_text[i])-97)-dk3)%26)+97)
                
            else:
                decrypt+=plain_text[i]
        print("Decrypted Text: " + decrypt)


if __name__ == "__main__":
    mc=MixCipher()
    mc.start_encrypt_decrypt()
