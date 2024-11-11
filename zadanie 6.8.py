#zadanie 6

#8
first = input('Enter first letter: ')
last = input('Enter last letter: ')
number_of_letters = abs(ord(last) - ord(first)) - 1
print(f'Between {first} and {last} is {number_of_letters} letters')