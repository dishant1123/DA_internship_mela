# loop  : 
"""
1. for 
2. while  
3. while true

"""

# for loop  : 

"""for i in range(10):
    print(i)

"""
# break  ,  contunie  pass 

# break : 
"""for i in range(10):
    if i==4 :
        break
    print(i,end=" ")
"""    
# contunie :
"""for i in range(10):
    if i==4 :
        continue
    print(i)
"""  
# pass :
"""for i in range(10):
    if i==4 :
        pass 
    print(i)
"""

# while  : 

"""i=1 
while i<=100 :
    print(i,end=" ")
    i+=1   # assingment operator
"""    


# pattern  : 
"""  
1.         2.           3.            4.               5.           6. 
*          * * * * *    * * * * *          *           * * * * *          *
* *        * * * *        * * * *         * *           * * * *         * * 
* * *      * * *            * * *        * * *           * * *        * * * 
* * * *    * *                * *       * * * *           * *       * * * *
* * * * *  *                    *      * * * * *           *      * * * * *

"""

# 1 : 

"""
for i in range(1,6) :   # row    3  ,6 
    for j in range(1,i+1) : # col  1,4 
        print('*',end=" ")   #  *
    print()                  #  * *
                             #  * * *  
"""                       
# 2 : 
"""
for i in range(1,6) :   # row    3  ,6 
    for j in range(6,i,-1) : # col  1,4 
        print('*',end=" ")   #  *
    print()                  #  * *
                             #  * * *  
"""

# 3 : 
"""
* * * * * 
  * * * * 
    * * * 
      * * 
        *
"""

"""for i in range(1,6) :   # row  3 ,6     
    for k  in range(1,i):     # 1,3
        print(" ",end=" ")   # 
    for j in range(6,i,-1) : # 6 , 2 ,-1  
        print('*',end=" ")   # * * * * * 
    print()                  #   * * * *  
                             #     * * *     
"""
# 5 : 

"""
for i in range(1,6) :   # row  3 ,6     
    for k  in range(1,i):     # 1,3
        print("",end=" ")   # 
    for j in range(6,i,-1) : # 6 , 2 ,-1  
        print('*',end=" ")   # * * * * * 
    print()                  #   * * * *  
                             #     * * *     
"""

# 6 :
"""
for i in range(1,6) :   # row    3  ,6 
    for k in range(5,i,-1):
        print(" ",end=" ")   #
    for j in range(1,i+1) : # col  1,4 
        print('*',end=" ")   #  *
    print()                  #  * *
"""

# 4 :

"""
for i in range(1,6) :   # row    3  ,6 
    for k in range(5,i,-1):
        print("",end=" ")   #
    for j in range(1,i+1) : # col  1,4 
        print('*',end=" ")   #  *
    print()                  #  * *
"""

# full diamond : 
for i in range(1,5) :   # row    3  ,6 
    for k in range(5,i,-1):
        print("",end=" ")   #
    for j in range(1,i+1) : # col  1,4 
        print('*',end=" ")   #  *
    print()                  #  * *

for i in range(1,6) :   # row  3 ,6     
    for k  in range(1,i):     # 1,3
        print("",end=" ")   # 
    for j in range(6,i,-1) : # 6 , 2 ,-1  
        print('*',end=" ")   # * * * * * 
    print()                  #   * * * *  
