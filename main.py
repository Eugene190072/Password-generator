import random

elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_len = int(input('Длина пароля'))

password = ''

for i in range(pass_len):
    password += random.choice(elements)

print(password)
