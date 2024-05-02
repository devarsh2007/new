# write a program that check vowels are exist in given string

string = input("enter string : ")
# print(string)

vowels = ["a","e","i","o","u"]

# ans = vowels[0] in string
# ans = vowels[1] in string
# ans = vowels[2] in string
# ans = vowels[3] in string
# ans = vowels[4] in string

ans = "a" in string
if(ans==True):
      print("a in message")
      
ans = "e" in string
if(ans==True):
      print("e in message")
      
ans = "i" in string
if(ans==True):
      print("i in message")
      
ans = "o" in string
if(ans==True):
      print("o in message")
      
ans = "u" in string
if(ans==True):
      print("u in message")
      
print("good bye")