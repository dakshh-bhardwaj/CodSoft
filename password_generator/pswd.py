import random
import string

def pswd(len):
    characters = string.ascii_letters + string.digits + string.punctuation
    passd = ''.join(random.choice(characters) for _ in range(len))
    return passd

length = int(input("Enter the length of the password: "))
new_pswd = pswd(length)
print("The new generated password is:", new_pswd)