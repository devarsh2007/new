# write a program that perform data entry
# student -> name,std,no

# [(name,std,no),(),()]

student=[]
number=int(input("enter total entry : "))

for i in range(1,number+1):
      print(f"\n------------------- student {i} ---------------------\n")
      name = input("enter student name : ")
      std = int(input("enter student std : "))
      no = int(input("enter student no : "))
      
      details = (name,std,no)
      # print(details)
      
      student.append(details)
      
print(student)
