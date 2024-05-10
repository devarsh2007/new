# write a program that calculate shiping cost

# weight , distance

# 50 = 100

weight = float(input("enter weight : "))
distance = int(input("enter distance in km : "))

if weight<=0 or distance<=0:
      print("invalid input")
      
else:
      if weight<=50:
            weight_cost=100
            
            if distance<=100:
                  cost = weight_cost+200
                  
            elif distance<=200:
                  cost=weight_cost+400
                  
            elif distance<=300:
                  cost=weight_cost+600
            
      elif weight>50:
            weight_cost=200
            
            if distance<=100:
                  cost=weight_cost+200
                  
            elif distance<=200:
                  cost=weight_cost+400
                  
            elif distance<=300:
                  cost=weight_cost+600
                  
      print("your shiping cost : ",cost)