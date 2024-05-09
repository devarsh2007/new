# write a program that print grad of students
# 80-100 = A
# 60-79 = B
# 40-59 = C
# 40> = D

marks = float(input("enter student marks : "))

if marks<0 or marks>100:
      print("invalid marks")
      
else:
      if marks>=80 and marks<=100:
            grad="A"
            
      elif marks>=60 and marks<80:
            grad="B"
            
      elif marks>=40 and marks<60:
            grad="C"
            
      elif marks<40:
            grad="D"
            
      print("your grad : ",grad)
            