#zadanie 7

#4
import math
circumference = float(input('Enter tree circumference in cm: '))
srednica = circumference / math.pi
can = srednica >= 50
print(f'Tree can be cut down: {can}')