class person():
      def walk(self):
            print("i can walk")
            
      def talk(self):
            print("i can talk")
            
class employee(person):
      def work(self):
            print("i can work")
            
      def make(self):
            print("i can make codes")
                
                
class student(employee):
      def read(self):
            print("i can read")
            
      def write(self):
            print("i can write")
            
s1 =student()
s1.read()
s1.write()
s1.walk()
s1.talk()
s1.work()
s1.make()