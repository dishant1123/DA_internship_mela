"""
python  : guido ven rossum  

comment  : # , double/single qutoes 3 time 

data type  : 
1.int  2.float 3.bool 4.complex 5. char/string 

python  data type  : 

1. list -----> mutable ----> ordered  ----> changes in list  
2. tuple ----> immutable  -----> orderted   ----> not changes in tuple 
3. dict  -----> mutable    ----> pair  ---->? key value   ----> key  ----> immutable  ----> value ---->mutable 
4. set  ---> mutable ---->unordered ----> changes in set ----> not  store duplicate value in set 
5.string  ----> immutable  ----> not changes in string

"""
"""
l1=[12,45,74,55,99]
# access index : start index : 0 

# update : 

l1[2] =900 
print(l1)
# insert : 
l1.insert(3,8090)
print(l1)
"""

"""t1=(12,78,63,99,4j,True)
print(t1)
print(type(t1))

# t2=12,78,63,99,4j,True
t2=12,
print(t2)
print(type(t2))  #
"""

"""d1={"name":"guido","age":25,"gender":"male"}
print(d1)
print(type(d1))

d1["develop","tisha_nagrani"]=["python","C++"]
print(d1)
"""
"""d2={34:89 ,"maynak" :34} 
# print(d2)
# print(d2.keys())
d2["maynak"]=99 
print(d2)
"""
# print(d2[1])  # in dict not access though  index.

# s3={"vansh","roshni","mayank","tisha_nagrani"}

# print(s3)
# print(type(s3))

# s4=set()
# s4={}
# print(s4)
# print(type(s4))


# set : set  is unordered so  we can't access index and slicing  in set. 

"""s1={12,45,74,55,99}
print(s1)
# print(s1[3:5]) 

s1.add(100) 
print(s1)
"""

#frozenset : its part of the  set but  frozen set is immutable you can't change it --->its also unordered ----> not store duplicate value

"""fz =frozenset({12,45,74,55,99})
print(fz)
print(type(fz))

"""

# string : immutable  ----> not changes in string

s1="guido ven rossum"
print(s1)
print(type(s1))

s2='12'
print(s2)
print(type(s2))

s3="my name is roshni singh and i am data analyst."

print(s3)
print(s3[1])
print(s3[1:2])
print(s3[-2])
print(s3[ : ])
print(s3[2 :8:2])
print(s3[ : :-1])