"""

This program is a password generator

"""

import secrets
import string
import re
import os

def clear():
    return os.system('cls')

def password_gen(lenght: int) -> str:
    if lenght < 6:
        lenght = 6

    # Password needs at least one upper case letter, one lower case, one number and one special character
    password_validator = re.compile(r'.*[A-Z].*[a-z].*[0-9].*[^A-Za-z0-9].*')
    characters = string.ascii_letters + string.digits + string.punctuation

    # Will generate passwords until they meet the criteria
    while True:
        password = ''
        
        for x in range(lenght):
            password += secrets.choice(characters)

        if re.match(password_validator, password):
            return password

if __name__ == '__main__':
    lenght = int(input('What lenght would you like your password to be?(min.: 6): '))
    clear()

    print(f'Password generated: {password_gen(lenght)}\n')