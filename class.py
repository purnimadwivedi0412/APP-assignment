class Person :

 def __init__(self, n, a, g):          
    self.name = n
    self.age = a
    self.gender = g

 def talk(self):
        print("Hi, I'm ", self.name)

 def vote(self):
        if self.age>18:
            print("I am eligible to vote.")
        else :
            print("I am not old enough to vote.")

p1= Person("riya", 20, "Female")
p2= Person("ajay", 19, "Male")

p1.talk()
p1.vote()
p2.talk()
p2.vote()