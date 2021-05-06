class Atbash:

    def __init__(self):
        self.user_input_1=""
    
    def start_atbash(self):
        user_input=str(input("Enter String to encrypt/decrypt: "))
        self.atbash_enc_dec(user_input)

    def atbash_enc_dec(self,user_input):
        my_table = {'A':'Z','B':'Y','C':'X','D':'W','E':'V','F':'U','G':'T','H':'S','I':'R','J':'Q','K':'P','L':'O','M':'N','N':'M',
    'O':'L','P':'K','Q':'J','R':'I','S':'H','T':'G','U':'F','V':'E','W':'D','X':'C','Y':'B','Z':'A'}
        cipher_message=""
        capital=user_input.upper()
        for letter in capital:

            if (letter != ' '):

                cipher_message+=my_table[letter]

            else:

                cipher_message+=' '
        print("Encrypted/Decrypted String: "+ cipher_message.lower())


if __name__== "__main__":
    ac=Atbash()
    ac.start_atbash()


