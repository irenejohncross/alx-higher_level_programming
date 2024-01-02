#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdigit = num % -10
else:
    lastdigit = num % 10
if lastdigit > 5:
    print("Last digit of {:d} is {:d} and is greater than five"
          .format(num, lastdigit))
Else if lastdigit < 6 and lastdigit != 0:
    print("Last digit of {:d} is {:d} and is less than six and not zero"
          .format(num, lastdigit))
else:
    print("Last digit of {:d} is zero and is zero".format(num))
