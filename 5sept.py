# oop : object oriented programming
"""
class : blue print  of  objects 

object :  instance  of  class 

ex : fruits    ------> apple , orange , banana , mango , pineapple

fruits ------> class 
apple,orange,banana,mango,pineapple  -------> objects

syntax : 

class name : 
    attribute1 = value1

object1 = class ()

public   : attribute  access any where ,update 
private   : attribute  access only in class  
protected : attribute  access only in class  and child class  (inheritance)


"""

# ex :1 
"""class student :  # student class name  
    name ="ravi"   # attributes  -----> name age   -----> public 
    age=23 
    
s=student()   # s object   -----> student  ----> class 
print("name  is  :",s.name)
print("age  is  :",s.age)
s.name = "raj"
s.age =24

print("name  is  :",s.name)
print("age  is  :",s.age)
"""

# ex :2   class function  : 

"""class student : 
    name ="ravi"
    age =21 
    
    def display(self) :  # self ----> keyword -----> class attributes , method  ----> access self
        print("name  is  :",self.name)
        print("age  is  :",self.age)

s=student()
s.display()
"""

# ex :3 private  : 

"""class employees : 
    name = "dhruv"  # name age  ----> public 
    age =21 
    __salary =90000   # salary  ----> private 
    
    def show(self):
        print("salary  is  :",self.__salary)
    
e=employees()
print("name  is  :",e.name)
print("age  is  :",e.age)  
# print("__salary  is  :",e.__salary) # error : bcz  of  private not  access though object 
e.show()
"""


# ex :4 protected  :

"""class student : 
    name  = "sahil"
    _age =21 # protected   ----> _ 
    
class teacher(student) :
    def display(self) :
        print("name  is  :",self.name)
        print("age  is  :",self._age)  # direct access ----> protected
        
t=teacher()
t.display()
"""

# constructor : automatically called when object is created .

"""
synatx : 

__init__ -----> constructor, special method 

3 type  : 

1. default  constructor
2. parameterized  constructor
3. non  parameterized  constructor

"""

# ex :1 

"""class student :
    def __init__(self):
        print("constructor")
        print("vansh  is  sitting beside me .")
        
s=student()  # s object  -----> student  ----> class
"""


# ex :2 non parameterized  constructor

"""class employees :
    def __init__(self):
        self.name  = "dhruv"  # name age ----> public 
        self.age =21 
    def show(self):
        print("name  is  :",self.name)
        print("age  is  :",self.age)
e=employees()
print("name  is  :",e.name)
print("age  is  :",e.age)
e.show()
e.name="raj"
e.age=22
e.show()
"""

# ex :3 parameterized  constructor

"""class employees :
    def __init__(self,name,age):
        self.name  = name
        self.age =age
    def display(self):
        print("name  is  :",self.name)
        print("age  is  :",self.age)
e=employees("vansh",34)
print("name  is  :",e.name)
print("age  is  :",e.age)
e.display()
"""
# destructor : when  object  is  deleted . 

"""
4 pillar : 

1. inheritance : derived class  inherit  attributes  and  methods  from  base  class 
    type  : 
    
    a. single  inheritance
        class a : 
        class b(a)
        
    b. multiple  inheritance
    
        class a 
        class b
        class c(a,b)
        
    c. multi level  inheritance
        class a 
        class b(a)   -----> b  object  ----> a
        class c(b)   ------> c object ---->a,b  access 

    d. hirearchy
        class a 
        class b(a)
        class c(a)
        class d(a)   ----> ex : ceo  ----> emp ----> ceo or manager

    e.hybrid :  its combination of  one or  more than one  inheritance
    
        class a 
        class b(a)
        class c(a)
        class d(c,d)   ----> combination  : multiple + multilevel 

2. polymorphism : many  form same function  different args 

    1. method  overriding :
        class animal :
            def sound(self):
                print("animal  is  sounding")
        class dog(animal):
            def sound(self):
                print("dog  is  barking")
        class cat(animal):
            def sound(self):
                print("cat  is  meowing")
                
        c=cat()   ------> meowing 
    
    2. method  overloading :
    
        class maths :
            def add(self,a,b):
                return a+b 
            def add(self,a):
                return a*2
            def add(self,a,b,c):
                return a+b+c
                
        m=maths()
        
        print(m.add(2,3))   # ---->1 function  call
        print(m.add(2))   # ---->2 function  call
        print(m.add(2,3,4))   # ---->3 function  call

3. encapsulation :

    1. get   : data receive  only  in  class
    2.set : private  attribute -----> modify  only  in  class

4. abstraction : data hide 

    ex : car driving  : 
    
from abc import ABC , abstractmethod ---->abc ---->abstract base class 

note : 

1. abstract class : not  create  object 
2. @abstractmethod : only declaration  
"""

# ex :1 
from abc import ABC , abstractmethod
"""
class car(ABC):
    name ="BMW"
    model ="X5"
    
    @abstractmethod
    def drive(self):
        pass 
    
class bmw(car):
    def drive(self):
        print("bmw  is  driving")
        
b=bmw()
b.drive()
"""

# class method  : 

"""
1. first  arg  : cls 
2. cls though  change  / modify  
"""
"""class student : 
    clg_name = "HL"
    
    @classmethod
    def show(cls,new_name):
        cls.clg_name = new_name
        print("name  is  :",cls.clg_name)

print("old  clg name is  (before change) :",student.clg_name)
student.show("AU")
print("new  clg name is  (after change) :",student.clg_name)

"""

# static method :funcion work  

"""
1. no changes / modify  in  class 
2. no self use in static method
"""

class maths :
    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def sub(a,b):
        return a-b
m=maths()
print(m.add(2,3))
print(m.sub(34,12))

# file handling  ,excepationl ,connective SQL   :