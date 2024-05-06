# write a program that print number in words
# 4 - four

number = int(input("enter a single digit number : "))

# l1=[1,2,3,4]
# d1 = {1:"one"}
# print(d1[1])

d1 = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}

# print(number in d1)
# print(d1[0])

if number in d1:
      print(d1[number])
      a=d1[number]
      # print(a[2])
      
else:
      print("invalid input")