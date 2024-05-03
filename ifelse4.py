# write a program that check given number is armstron or not

number = (input("enter a 3 digit number : "))

# 153
# print(number[0])
# print(number[1])
# print(number[2])

# print(number[0]*number[0]*number[0])
# print(type(first))
first = int(number[0])
second = int(number[1])
third = int(number[2])

print("------------------------------------")
# print(first*first*first)

# base ** 100

answer = (first**3) + (second**3) + (third**3)
# print("answer",answer)

number=int(number)

if(number==answer):
      print("it is armstron number")
      
else:
      print("it is not armstrong number")