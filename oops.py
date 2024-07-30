#OOPS CONCEPT
#First program
'''class student:
    name="xyz"
    age=0
    def study(self):  
        print("study hard",self.name)
obj=student()
obj.study()'''

#second program
'''class student:
    name="xyz"
    age=0
    def study(self):  
        print("study hard")
        self.sleep()

    def sleep(self):
        print("sleep 1 hour")
obj=student()
obj.study()'''
#third program
'''class student:
    name="xyz"
    age=0
    def study(self):  
        print("study hard")

    def sleep(self):
        print("sleep 1 hour")
        study()
obj=student()
obj.study()'''

'''#Inheritance
#multilevel inheritance
class A:
    def show(self):
        print("This is show method")
class B(A):
    pass
class C(B):
    pass
#Hirerachical inheritance
class A:
    def show(self):
        print("This is show method")
class B(A):
    pass
class C(A):
    pass

#Hybrid inheritance
class A:
    def show(self):
        print("This is show method")
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass'''

#Inheritance exaple
'''class A:
    def show(self):
        print("This is show method")
class B(A):
    def demo(self):
        print("demo method")
class C(A):
    pass
class D(B,C):
    pass
obj=C()
obj.show()
obj.demo()#error'''

#Polymorphism
#Python does not support method overloading
'''def setData(a,b,c):
    print(a+b+c)
setData(2,3,1)
setData(2,1)'''

'''Over riding-Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class.
In inheritance, the child class inherits the methods from the parent class. 
However, it is possible to modify a method in a child class that it has inherited from the parent class. 
This is particularly useful in cases where the method inherited from the parent class doesn't quite fit the child class.
In such cases, we re-implement the method in the child class. 
This process of re-implementing a method in the child class is known as Method Overriding.'''

'''class bird:
    def intro(self):
        print("There are many types of birds.")
    def flight(self):
        print("Most of the birds can fly but some cannot")
class sparrow(bird):
    def flight(self):
        print("I can fly")
class ostrich(bird):
    def flight(self):
        print(" I can't fly")

obj=sparrow()
obj.flight()'''

# Encapsulation
'''class A: 
    def __init__(self, age = 0,name=" "): 
         self._age = age 
         self._name = name
    # getter method 
    def get_age(self): 
        return self._age 
    def get_name(self): 
        return self._name 
    # setter method 
    def set_age(self, x): 
        self._age = x 
    def set_name(self, x): 
        self._name = x 
  
obj = A() 
obj.set_age(21)
obj.set_name("lucky") 
print(obj.get_age()) 
print(obj.get_name())'''



  
