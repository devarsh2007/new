print("1->product1")
print("2->product2")
print("3->product3")

choise = int(input("enter your choise : "))

if choise==1:
      file = open("bill.py","a")
      file.write("\nproducts.append(('product1',1000,5))")
      file.close()
      print("product added....")
      
elif choise==2:
      file = open("bill.py","a")
      file.write("\nproducts.append(('product2',5000,10))")
      file.close()
      print("product added....")
      
elif choise==3:
      file = open("bill.py","a")
      file.write("\nproducts.append(('product3',10000,3))")
      file.close()
      print("product added....")
      
else:
      print("invalid input")