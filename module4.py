import random 

# 1.random 0 - 1
print(random.random())

# 2.uniform min - max
print(random.uniform(10,11))

# 3.randint min-max int
print(random.randint(10,20))

# 4.randrange
print(random.randrange(0,50,10))

# 5.choise
colours = ["red","blue","green","yellow","black"] 
print(random.choice(colours))

# 6.shuffle
numbers = [1,2,3,4,5]
random.shuffle(numbers)
print(numbers)