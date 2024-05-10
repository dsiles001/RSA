import random
import sympy
import math
import egcd

def makeKeys():
    i = 0
    while i !=2:
        num = random.randint(1,1000) # edit prime number size limits here
        if sympy.isprime(num):
            if i == 0:
                p = num
            else:
                q = num
            i+=1

    # print(p)
    # print(q)
    n = p*q
    phi = (p - 1) * (q - 1)

    for i in range(2, phi):
        if math.gcd(i, phi) == 1:
            e = i
            d = egcd.egcd(e, phi)[1] % phi
            return n,e,d 
    raise ValueError("No suitable e found")
    return ("[ERROR] There was an error in the key generation process. Run again")



def TextToAscii(message):
    ascii = ""
    for letter in message:
        ascii += str(ord(letter))
    return int(ascii)

def AsciiToText(asciis):
    message = ''
    for ascii in asciis:
        message += chr(ascii)

    return message


def encrypt(n, e, message):

    encrypted = []
    for char in message:
        c = TextToAscii(char)
        encrypted.append(pow(c, e, n))

    return encrypted

    
def decrypt(ciphertext, n, d):

    decrypted = []

    for c in ciphertext:
        decrypted.append(pow(c,d,n))
    return decrypted


if __name__=='__main__':


    choice = int(input("Are you sending(1) or receiving(2) a text: "))

    if choice == 1:
        n, e = input("What is the receiver's public keys. Seperate with space->(n e): ").split()
        n, e = int(n), int(e)
        message = input("What is the message you would like to send: ")
        ciphertext = encrypt(n, e, message)
        print(f'Give the ciphertext to the recipient: {ciphertext}')



    elif choice == 2:
        #receiving logic
        n, e, d = makeKeys()
        print('Give these values to the sender:')
        print(f'n value: {n}')
        print(f'e value: {e}')
        ciphertext = input("What are the ciphertext values: ").split(", ")
        ciphertext = list(map(int, ciphertext))
        decrypted = decrypt(ciphertext,n,d)
        message = AsciiToText(decrypted)
        print(message)


    else:
        print("Not an option")
