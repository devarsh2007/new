def simple_interest(p,r,t):
      si = (p*r*t)/100
      print("total iterest : ",si)
      print("total amount : ",si+p)
      
p = int(input("enter amount : "))
r = int(input("enter rate : "))
t = int(input("enter time in years : "))

simple_interest(p,r,t)
