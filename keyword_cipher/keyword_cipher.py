class Keyword:

    def __init__(self):
        self.user_input=""
    def start_encrypt_decrypt(self):
        choice=int(input("Enter 1 for Encryption and 0 for Decryption: "))
        if (choice == 1):
            self.encrypt()
        elif (choice== 0):
            self.decrypt()
        else:
            print("Pls Enter Valid Number!")
            

    
    def encrypt(self):
        user_input=input("Enter text to be encrypted: ").lower()
        valid_letters="abcdefghijklmnopqrstuvwxyz "
        user_key=input("Enter key to be used for encryption: ").lower()
        key=""

        new_string= ""
        cipher_txt=""  

        for char in user_input:
            if char in valid_letters:
                new_string+=char

        for char in user_key:
            if char in valid_letters:
                if char not in key:
                    key += char
        
        for char in valid_letters:
            if char not in key:
                key+=char
        
    
        for letter in new_string:
            old_index=valid_letters.index(letter)
            new_letter=key[old_index]
            cipher_txt+=new_letter


        print("Encrypted String: " + cipher_txt)
    

    def decrypt(self):
        user_input=input("Enter text to be decrypted: ").lower()
        valid_letters="abcdefghijklmnopqrstuvwxyz "
        user_key=input("Enter key to be used for decryption: ").lower()
        key=""

        new_string= ""
        uncipher_txt=""  

        for char in user_input:
            if char in valid_letters:
                new_string+=char

        for char in user_key:
            if char in valid_letters:
                if char not in key:
                    key += char
        
        for char in valid_letters:
            if char not in key:
                key+=char
        
    
        for letter in new_string:
            old_index=key.index(letter)
            new_letter=valid_letters[old_index]
            uncipher_txt+=new_letter


        print("Decrypted String: " + uncipher_txt)


if __name__ == "__main__":
    kc=Keyword()
    kc.start_encrypt_decrypt()
