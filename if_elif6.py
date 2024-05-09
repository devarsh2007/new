# write a program that print zodiac sign

date = int(input("enter your birth date : "))
month = int(input("enter your birth month : "))

# if date>31 or date<1 or month>12 or month<1:
#       print("invalid input")

if date>31 or date<1 :
      print("invalid date")
      
elif month>12 or month<1:
      print("invalid month")
      
elif (month==3 and date>=21) or (month==4 and date<=19):
      print("zodiac sign : aries")
      
elif (month==4 and date>=20) or (month==5 and date<=20):
      print("zodiac sign : taurus")
      
elif (month==5 and date>=21) or (month==6 and date<=20):
      print("zodiac sign : gemini")
            