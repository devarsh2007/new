class person():
      def walk(self):
            print("i can walk")
            
      def talk(self):
            print("i can talk")
                
                
class student(person):
      def read(self):
            print("i can read")
            
      def write(self):
            print("i can write")
            

s1 = student()
s1.read()
s1.write()
s1.walk()
s1.talk()