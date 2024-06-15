
def find_vowels_consonate(message):
      v1 = ["a","e","i","u","o"]
      vowels=0
      consonate=0
      for i in message:
            if i in v1:
                  vowels+=1
            
            else:
                  consonate+=1
                  
      print("total vowels : ",vowels)
      print("total consonate : ",consonate)
                  
m=input("enter a message : ")
find_vowels_consonate(m)
