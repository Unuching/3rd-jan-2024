import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
symbols = symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]


print("Welcome to python password generator!")

nr_letters = int(input("How many letters do you want in your password?"))
nr_numbers = int(input("How many numbers do you want?"))
nr_symbols = int(input("How many symbols do you want?"))


password = []

for char in range(1, nr_letters+1):
    password += random.choice(letters)
for char in range(1, nr_numbers +1):
    password += random.choice(numbers)
for char in range(1, nr_symbols +1):
    password += random.choice(symbols)

random.shuffle(password)

pass_ = " "

for char in password:
    pass_ += char

    
print(pass_)