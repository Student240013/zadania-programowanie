#1 zadanie

#1
a = 5
h = 4
pole = 0.5 * a * h
print("pole trojkata wynosi:", pole)

#2
numery = [7, 12, 31]
średnia = sum(numery) / len(numery)
print("srednia wynosi:", format(średnia, ".2f"))

# 2 zadanie

#1
# + --> konkatenacja napisów
# * --> powielenie znaków
# ** --> potęgować
# / --> dzielić
# // --> ile razy się mieści liczba
# % --> reszta z dzielenia
# > --> wieksze niz
# <= --> mniejsza badz rowne od

#2
a = 3
b = 2
c = 1
wynik = a * b + c
print("3 * 2 + 1 wynosi", wynik)

#3
a=5
b=10
c=5
wynik = a + b * c
print("5 + 10 * 5 wynosi", wynik)

#4
a=4
b=2
wynik = a + a / b ** b
print("4 + 4 / 2 ** 2 wynosi", wynik)

#5
a=4
b=3
c=2
d=1
wynik = a % b % c % 1
print("4 % 3 % 2 % 1 wynosi", wynik)

#6
a=1
b=2
c=3
d=4
e=5
wynik = a + b % c ** d * e
print("1 + 2 % c ** d * e wynosi", wynik)

#7
a=True
b=False
wynik = a != b
print("true != false wynosi", wynik)

#8
# int 50, float 149.17, int 4*7, float 4.0*7, str "Krakow University of Economics", bool true, int 2>5

#3 zadanie

#1
company = "ABC Data"
phone = "555-123-009"
employees = 25
remote_work = True
big_company = employees > 100
income = 4500000
income_per_person = income / employees
print(income_per_person)
# 7 zmiennych - company,    phone,    employees, remote_work, big_company, income, income_per_person
# 7 wartosci - "ABC Data", "555-123-009", 25,     true,        false,      4500000,   180000.0
#7 typow -      str             str       int     bool          bool         int        float

#2
number1 = 71
number2 = 14
number3 = 20
result = number1 + number2 + number3

print('Number 1:', number1)
print('Number 2:', number2)
print('Number 3:', number3)
print('The result of summation:', result)

#3
x = 7
y = 34
z = 0 
print("Before swapping: x=", x, "y=", y)

z = x
x = y
y = z

print("After swapping: x=", x, "y=", y)

#4
speed_kmh = 70
speed_ms = speed_kmh * 1000 / 3600
print(speed_kmh, "km/h =", speed_ms, "m/s")

#5
import math

a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2)
print("Długość przekątnej wynosi:", diagonal)

#6
import math
h = 1.75
h_hotel = 20
dystans_plaza = 3.57 * math.sqrt(h)
dystans_hotel = 3.57 * math.sqrt(h_hotel)
print("dystans do horyzontu z plazy wynosi",dystans_plaza, "km")
print("dystans do horyzontu z hotelu wynosi", dystans_hotel, "km")

#7
total = 8000000000
north = 7200000000
south = total - north
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", north/total*100)
print("Southern Hemisphere population: ", south)
print("Southern Hemisphere percentage: ", (south / total) * 100)

#8
math = 5
art = 4
music = 5
history = 3
average = (math + art + music + history) / 4
print("Average grade is:", average)

#4 zadanie

#1
name = "Adam"
age = 19
h = 175
print(f"My name is, {name}.")
print(f"I am {age} years old, and my height is {h} cm.")
print(f"In 6 years i will be {age + 6} years old.")

#2
father_income = 5450
mother_income = 4920
family_members = 5
total_income = father_income + mother_income
income_per_person = total_income / family_members
print(f'Total family income is {total_income} and income per person is {income_per_person}')

#3
a = 3
b = 5
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')

#zadanie 6

#1
name = 'Bartosz'
surname = 'Walasek'
characters_in_name = len(name)
characters_in_surname = len(surname)
full_name = name + ' ' + surname
characters_in_full_name = len(full_name)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {characters_in_surname} characters')
print(f'Your full name has {characters_in_full_name} characters')

#2
name = 'Bartosz'
surname = 'Walasek'
print(name[0] + surname[0])

#3
university = "Krakow University of Economics"
abbreviation = university[0] + university[7] + university[21]
print(abbreviation)

#4
employee = "Mr. John May, born on 1998-02-16"
name = employee[4:8]
surname = employee[9:12]
dob = employee[-10:]
initials = name[0] + surname[0]
print(f'Name: {name}')
print(f'Surname: {surname}')
print(f'Born: {dob}')
print(f'Initials: {initials}')

#6
print(f'a {ord('a')}')
print(f'b {ord('b')}')
print(f'z {ord('z')}')
print(f'A {ord('A')}')
print(f'B {ord('B')}')
print(f'Z {ord('Z')}')
print(f'1 {ord('1')}')
print(f'= {ord("=")}')
print(f'+ {ord("+")}')
print(f'€ {ord("€")}')

#7
name = 'Bartosz'
print(f'The letter {name[0]} has a code {ord(name[0])}')
print(f'The letter {name[1]} has a code {ord(name[1])}')
print(f'The letter {name[2]} has a code {ord(name[2])}')
print(f'The letter {name[3]} has a code {ord(name[3])}')
print(f'The letter {name[4]} has a code {ord(name[4])}')
print(f'The letter {name[5]} has a code {ord(name[5])}')
print(f'The letter {name[6]} has a code {ord(name[6])}')

#9
print(chr(67), chr(111), chr(111), chr(108), chr(33))

#10
movie = "The Lord of the Rings: The Return of the King"
print('Number of characters: ', len(movie))
print('Title in capital letters: ', movie.upper())
print('Title in small letters: ', movie.lower())
print('Number of times "e" appears: ', movie.lower().count('e'))
print('Position of "Lord": ', movie.find("Lord"))
print('Position of "dragon": ', movie.find("dragon"))

#zadanie 7

#8
import random
dice_roll_1 = random.randint(1, 6)
dice_roll_2 = random.randint(1, 6)
dice_roll_3 = random.randint(1, 6)
total = dice_roll_1 + dice_roll_2 + dice_roll_3
print(f'Dice roll 1: {dice_roll_1}')
print(f'Dice roll 2: {dice_roll_2}')
print(f'Dice roll 3: {dice_roll_3}')
print(f'Total sum of dice rolls: {total}')

#9
import random
dice_roll = random.randint(1, 6)
special_number = dice_roll == 1 or dice_roll == 6
print(f'Dice rolled: {dice_roll}')
print(f'Special number (1 or 6): {special_number}')

#10
import random
computer = random.randint(1, 6)
you = int(input('Guess the number rolled by the computer (1 to 6): '))
won = you == computer
print(f'You won: {won}')
