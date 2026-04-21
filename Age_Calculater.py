import datetime

now = datetime.datetime.now()
year = now.year


age = int(input('Enter Your birth year: '))


rx = year - age
print('Your age is:', rx)


if rx == 20 or rx == 21 or rx == 22 or rx == 23 or rx == 24 or rx == 25 or rx == 26 or rx == 27 or rx == 28 or rx == 29 or rx == 30 or rx == 31 or rx == 32:
    print('Enjoy your youth')

elif rx == 33 or rx == 34 or rx == 35 or rx == 36 or rx == 37 or rx == 38 or rx == 39 or rx == 40 or rx == 41 or rx == 42 or rx == 43 or rx == 44 or rx == 45:
    r = input('Have you finished paying off your personal loan? (yes/no): ').lower()
    if r == 'yes':
        print('That’s good')
    else:
        print('Sorry for that')
elif rx == 46 or rx == 47 or rx == 48 or rx == 49 or rx == 50 or rx == 51 or rx == 52 or rx == 53 or rx == 54 or rx == 55:
     print('Enjoy your retirement')          