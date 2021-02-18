class Person:

  balance = 2000
  
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender
    self.balance = self.iterate(self.balance)

  def myname(self):
    print("Hello my name is " + self.name)

  def myage(self):
    print("My age is " + str(self.iterate(self.age)))

  def mygender(self):
    print("My gender is " + self.gender)

  def mybalance(self):
    print("My balance is " + str(self.balance))

  def iterate(self, x):
    return x + 1

class Student(Person):
  def __init__(self, name, age, gender, grade):
    # Person.__init__(self, age, gender)
    super().__init__(name, age, gender)
    self.age += 1
    self.grade = grade
    self.graduationyear = 2019

  def mygrade(self):
    print("My grade is " + str(self.grade))

  def mygraduationyear(self):
    print("My graduation year is " + str(self.graduationyear))


# -------------------------

p1 = Person("John", 36, "Male")
p1.myname()
p1.myage()
p1.mygender()
p1.mybalance()
p1.balance += 1000
p1.mybalance()

print()

p2 = Person("Laura", 16, "Female")
p2.myname()
p2.myage()
p2.mygender()
p2.mybalance()
# p2.mygrade()

print()

p3 = Student("Bill", 13, "Male", 4)
p3.myname()
p3.myage()
p3.mygrade()
p3.mygraduationyear()