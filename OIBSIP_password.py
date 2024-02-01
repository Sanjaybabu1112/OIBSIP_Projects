import random
import string

def get_input():
    try:
        length=int(input("\nEnter the length for the password: "))
        letters=input("Include letter? (y/n): ").lower()=='y'
        num=input("Include numbers? (y/n): ").lower()=='y'
        symbol=input("Include symbols? (y/n): ").lower()=='y'

        return length, letters, num, symbol
    
    except ValueError:
        print("Error: Enter valid input for the password length!")
        return None
    
def gen_password(length, letters=True, num=True, symbol=True):
    char=""
    if letters:
        char += string.ascii_letters
    if num:
        char += string.digits
    if symbol:
        char += string.punctuation
    
    if not char:
        print("Error: Please select atleast one of the options!")
        return None
    
    password = ''.join(random.choice(char) for _ in range(length))
    return password

def main():

    user_in = get_input()

    while user_in == None:
        user_in = get_input()

    length, letters, num, symbol = user_in
    password = gen_password(length, letters, num, symbol)

    if password:
        print("Generated Password: ", password)

if __name__ == "__main__":
    main()