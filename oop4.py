class person():
      def __init__(self,name,age):
            print("constructor called....")
            self.name = name
            self.age = age
            
      def write(self,a,b):
            print("write function called....")
            print(self.name)
            print(self.age)
            print(a)
            print(b)
             

p1=person("raam",28)
p1.write(2,3)

