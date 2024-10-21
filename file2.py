file = open("file1.py",'r')
text = file.read()
print(text)

file.close()

print("-"*50)

file2 = open('calculator.py','r')
text2 = file2.read(20)
print(text2)
file2.close()

new = open('demo.txt','w')
new.write('new data ')
new.write('\nnew data 2')
print("data witten on file")
new.close()