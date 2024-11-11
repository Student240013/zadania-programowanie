#zadanie 8

#4

swift = input('Enter the SWIFT code: ')
bank = swift[:4]
country = swift[4:6]
location = swift[6:8]
branch = swift[8:11]
print(f'Bank Code: {bank}')
print(f'Country Code: {country}')
print(f'Location Code: {location}')
print(f'Branch Code: {branch}')