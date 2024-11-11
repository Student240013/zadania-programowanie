#zadanie 7

#10
import random
computer = random.randint(1, 6)
you = int(input('Guess the number rolled by the computer (1 to 6): '))
won = you == computer
print(f'You won: {won}')