# lambda : 
"""
one  liner function . 

syntax : 
lambda arg : expression 
"""

# ex :1 

"""
def add(e,y):
    return e+y
print(add(2,3))

result = lambda a,b : a+b
print(result(2,3))
"""

# ex :2 
"""def big(a,b):
    if a>b :
        print("a is greater")
    else :
        print("b is greater")
big(23,45)
"""
# r =lambda a,b :print("a is  big")  if a>b else print("b is greater")
# r =lambda a,b :a  if a>b else b
# print(r(23,45))
"""
y =lambda a,b,c : max(a,b,c)
print(y(23,45,67))
"""

# filter : 

"""
l1=[1,2,3,4,5,6,7,8,9]
odd=[]
even=[]

for i in l1 :
    if i % 2==0 :
        even.append(i)
    else :
        odd.append(i)
print(odd)
print(even)
"""
"""
l1=[1,2,3,4,5,6,7,8,9]

r=list(filter(lambda x : x % 2==1,l1))
r1=list(filter(lambda x : x % 2==0,l1))

print(r)
print(r1)
"""

# filter  : 

l1=["maam","php","java","c","python","1221"]
# print  pelindrome string  : 
"""l2=[]
for i in l1 :  #  php 
    if i == i[ : : -1]:   # if "php"==  "php"  
        l2.append(i)   # maam 
print(l2)   
"""
"""e2=tuple(filter(lambda x :x == x[ : : -1],l1))
print(e2)
"""

# map  : it given  new list . 
# print  square of l1. 

"""l1=[14,23,35,4,56,5,6]    #  -----> changes : 228 , 560 , 700 ,16 

r =list(map(lambda x : x**2,l1))
print(r)
"""

#recursion  function  : function  call  itself .

"""
factorial  : 5!  -----> 5 * 4!  -----> n * (n-1) ! 
"""

"""def facto(n):   # 1 
    if n==1 :      # if 1==1 
        return 1 
    else :
        return n* facto(n-1)   # 2 * facto(1)  ---->120 
print(facto(5))
"""

"""def n_sum(n):  # 5 
    if n==1 :   # 
        return 1 
    else :
        return n + n_sum(n-1) 
print(n_sum(5))
"""

# reduce module :


# next : packages , oop : 