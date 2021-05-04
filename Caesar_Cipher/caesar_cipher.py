class CaesarCipher:

    def __init__(self):
        self.user_input_1= ""
        self.true_key= 0
        self.enc_or_dec =0

    def Enc_dec(self):
        self.user_input_1=user_input=input("Enter String to be encoded/decoded: ")
        self.true_key=key=int(input("Enter key for encryption/decryption of string: "))
        self.enc_or_dec=enc_dec=int(input("Enter 1 for encrytion and 0 for decryption: "))
        if (enc_dec == 1):
            self.enc(user_input,key)
        elif (enc_dec == 0):
            self.dec(user_input,key)
        else:
            print("Please choose from available options!")
        
    def enc(self,user_input,key):
        encrypted=""
        letter=''
        for letter in user_input:
            if(ord(letter)>=65 and ord(letter)<=90):
                letter=chr((((ord(letter)-65)+key)%26)+65)
                encrypted=encrypted+letter
            elif(ord(letter)>=97 and ord(letter)<=122):
                letter=chr((((ord(letter)-97)+key)%26)+97)
                encrypted=encrypted+letter
            else:
                encrypted=encrypted+letter
        print(encrypted)




    def dec(self,user_input,key):
        decrypted=""
        letter=''
        for letter in user_input:
            if(ord(letter)>=65 and ord(letter)<=90):
                letter=chr((((ord(letter)-65)-key)%26)+65)
                decrypted= decrypted+letter
            elif(ord(letter)>=97 and ord(letter)<=122):
                letter=chr((((ord(letter)-97)-key)%26)+97)
                decrypted= decrypted+letter
            else:
                decrypted=decrypted+letter
        print(decrypted)
    

if __name__ == "__main__":
    ct=CaesarCipher()
    ct.Enc_dec()