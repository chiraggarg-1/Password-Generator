import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','&','(',')','*','+']

print("WELCOME TO PASSWORD GENERATOR!")
n_letter = int(input("How Many Letters Would You Like In Your Password? "))
n_symbols = int(input("How Many Symbols You want in Your Password? "))
n_numbers = int(input("How many Numbers You want in Your Password? "))
password_list = []

for i in range(1,n_letter+1):
    char = random.choice(letters)
    password_list += char
    i += 1


for i in range(1,n_symbols+1):
    char = random.choice(symbols)
    password_list += char
    i += 1


for i in range(1,n_numbers+1):
    char = random.choice(numbers)
    password_list += char
    i += 1
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ''
for i in password_list:
    password += i
print(password)

