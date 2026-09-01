# function  : 
"""
syntax : 

def function_name() :
    code  
    
call()  
type  : 

1. no  arg no return 
2. no  arg  with  return
3. with  arg no return
4. with  arg  with  return

"""

# ex :1 no arg  no return 

"""def add() :  # add function name  
    a=int(input("enter a number : "))   # function  intialization  
    b=int(input("enter a number : "))
    print("sum is : ",a+b)
    
add()  # calling  
add()
add()
print("tisha not attending  morning session  bcz of sleeping issue.")
add()
print("mayank is  intelligent boy .")
add()
print("sujal is  future assistant of vansh sir.")
"""

# ex :2 with arg  no return

"""
def add(a,b) :  # a, b paramaters
    print("sum is : ",a+b)
    
add(23,56)
add(34.78 ,90.56)
add("sujal","sharma")
"""

# ex :3 no arg  with return
"""
def add() :
    a=int(input("enter a number : "))
    b=int(input("enter a number : "))
    return a+b 

print(add())
"""
# ex :4 with arg  with return

"""def add(a,b):
    return a+b
print(add(23,56))
"""

# ex :6 check  prime  number using  function  

"""def check_prime(n):
    count =0 
    
    for i in range(1,n+1):
        if n % i ==0 :
            count +=1
    if count ==2:
        return True
    else:
        return False
    
print(check_prime(19))
"""

# ex :7 local  variable : access only inside  function

"""
def x() :
    a=90 
    print(a)
x()
# print(a)  # bcz of a is  local  variable  so  it  can't  be  accessed  outside  function
"""

# ex :8 global  variable : access  everywhere
"""a=80
def x() :
    print(a)
x()
print(a)
"""

# ex :9 global variable can be modify using global keyword
"""y=90
def xy():
    global y 
    y=900 
    print(y)
xy()  # 900
print(y)  #90 
"""

# ex : 10 *args : -----> only takes a number args . 
"""
def add(*args):
    return sum(args)

print(add(23,56))
print(add(23))
print(add(23,50,90))
print(add(23,45,67,89,12,34,56.89))
"""

# ex :11 **kwargs : -----> takes key value args.

def d(**kwargs):
    for i ,j in kwargs.items(): 
        print(f'{i} is {j}')
d(name="sujal",age=22,gender="male",city="rajstan",bestfriend="vansh")