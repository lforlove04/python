

import random
number = random.randint(1, 10)

player_name = input("Hallo,siapa namamu")
number_of_guesses = 0
print('oke! saya menebak angka 1 dan 10:')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('tebakanmu terlalu rendah')
    if guess > number:
        print('tebakanmu terlalu tinggi')
    if guess == number:
        break
if guess == number:
    print('anda menebak nomor di ' + str(number_of_guesses) + ' percobaan!')
else:
    print('anda tidak menebak nomornya, nomornya adalah ' + str(number))
