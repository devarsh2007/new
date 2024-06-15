
def print_table(s,e):
      for j in range(s,e+1):
            print(f"---------------- table {s} ----------------\n")
            for i in range(1,11):
                  print(f"{s} x {i} = {s*i}")
                  
            s+=1
            
print_table(1,0)
            
      