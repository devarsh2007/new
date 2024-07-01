# write a program that generetes a random password

import random as r
# r.choise()
# choise()

from random import *

password = ""
for i in range(10):
      password+=str(randint(0,9))
print(password)

# a="1"
# b="b"
# print(a+b)