class RailFence:

    def __init__(self):
        self.user_input_1=""

    def start_encrypt(self):
         user_input=input("Enter String to Encrypt:")
         key=4
         self.encrypt(user_input,key)

    def encrypt(self,user_input,key):
        encrypted=""
        block1=""
        block2=""
        block3=""
        block4=""

        for i in range(len((user_input))):
            if(i%2==0 and i%3==0):
                block1=block1+user_input[i]
            elif(i%2!=0 and i%3!=0):
                block2=block2+user_input[i]
            elif(i%2==0 and i%3!=0):
                block3=block3+user_input[i]
            elif(i%2!=0 and i%3==0):
                block4=block4+user_input[i]

        encrypted=block1+" "+block2+" "+block3+" "+block4

        print("Encrypted String:"+ encrypted)


if __name__ == "__main__":
    rf=RailFence()
    rf.start_encrypt()