import mysql.connector as con

db = con.connect(host="localhost",user='root',password='',database='py18')
print("connection established.....")

mycursor=db.cursor()

# id=int(input("enter id :"))
# age=int(input("enter age : "))
# mobile = int(input("enter mobile : "))


# data = [id]

sql = "select * from student"

mycursor.execute(sql)

# db.commit()
# print("row added..........")
# print("row deleted......")
data = mycursor.fetchall()
print(data)