import random

print('Welcome To Password Generator')

chars ='abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ!#$%&*+,-./0123456789:;<=>?@'  

number = input('Amount of passwords genera: ')    
number = int(number)

length = input('Input your password length: ')
length = int(length)

print('\nhere are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)