file1 = open('exeption4.py')
print(file1)
print("file1-------------------------")
for i in file1:
    print(i)
    
print("\nfile2-------------------------")
f2 = open('calculator.py')
for i in f2:
    for j in i:
        if j=='t':
            print("-"*100)
            break
        
            
        else:
            print(j)
