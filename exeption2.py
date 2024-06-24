
try:
      file = open("demo4.txt","r")

      a=file.read()
      print(a)

      file2 = open("demo2.txt","w")
      file2.write(a)
      print("text added....")

      file.close()
      file2.close()
      
except:
      print("error : some error ocured")