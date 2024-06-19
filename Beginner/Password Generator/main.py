import random
import string


print('Welcome to the PyPassword Generator!')
letter_count = int(input('How many letters would you like in your password?\n'))
symbol_count = int(input('How many symbols would you like?\n')) 
number_count = int(input('How many numbers would you like?\n')) 

letters = ''.join(random.choices(string.ascii_letters, k=letter_count))
symbols =  ''.join(random.choices(string.punctuation, k=symbol_count))
numbers = ''.join(random.choices(string.digits, k=number_count))


password = letters + symbols + numbers
password_list = list(password)
random.SystemRandom().shuffle(password_list)
password_final = ''.join(password_list)

print(f'Here is your password: {password_final}')
