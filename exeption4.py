try:
    date = int(input("enter birth date : "))
    month = int(input("enter birth month : "))
    year = int(input("enter birth year : "))
    cy = 2024

    if(date<1 or date>31):
        raise ValueError 

    elif(month<1 or month>12):
        raise IndexError

    elif(year>=cy):
        raise KeyboardInterrupt

    age = cy - year

    if(age<18):
        raise TypeError

    else:
        print("congartulations.....")
    
except ValueError:
    print("error : invalid date")

except IndexError:
    print("error : enter valid month")

except KeyboardInterrupt:
    print("error : year does not exist")

except TypeError:
    print("error : not eligible")

finally:
    print("termineted")