
      
try:
      p = int(input("enter amount : "))
      r = int(input("enter rate : "))
      t = int(input("enter time in years : "))

      ans = (p*r*t) / 100

      print(ans)
      
except:
      print("you got an error")
      
print("this is some important code")