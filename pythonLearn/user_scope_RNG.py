import random

number_as_string1 = int(input('Pick a number '))

number_as_string2 = int(input('Pick another number '))

if number_as_string1 <= number_as_string2:
    r = random.randrange(number_as_string1, number_as_string2)
    print(r)
elif number_as_string1 > number_as_string2:
    r = random.randrange(number_as_string2, number_as_string1)
    print(r)