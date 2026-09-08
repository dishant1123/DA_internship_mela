# file handling  : 
"""
1. read   : exiting  file  
2. write  : new file created + write  ----> exiting  file open  ----> overwrite  file
3. append : new file created + write  ----> exiting  file open  ----> add in to the  file

1. fopen : open file
2. fclose : close file

"""

# w mode  : 
"""
with open("tisha.txt","w") as f :
    f.write("my name is tisha Nagrani.\n")
    f.write("my age is 22.\n")
    f.write("my hobby is sleeping.\n")
    f.write("best friend name is  sujal.\n")
    f.write("dream to meet Rahul Gandhi.")
    f.close()
"""
# write  mode  exiting file  : 
"""
with open("tisha.txt","w") as f :
    f.write("live in india.\n")
    f.write("love pizza.\n")
    f.write("very very  intelligent.\n")
    f.close()
"""

# read  : exiting file 

"""with open("tisha.txt","r") as f :
    # context = f.read()  # 5 
    # context = f.readline()
    context = f.readlines()
    
    print(context)
"""

# append : new file created + write  ----> exiting  file open  ----> add in to the  file

"""
with open("tisha.txt","a") as f :
    f.write("dushman name is vansh.\n")
    f.close()
"""
# a : 
"""with open("sujal.txt","a") as f :
    f.write("my name is sujal sharma.\n")
    f.write("study  in INTERNATIONAL SCHOOL.\n")
    f.write("made in rajasthan.\n")
    f.close()
"""
# r +  : write + read  -----> exiting 

"""with open("sujal.txt","r+") as f :
    f.write("Jay shah")
    f.seek(0)
    
    context = f.read()
    print(context)
    
    f.close()
    
# my name is sujal sharma. ---> len  --->23 
# Jay shah   ----> len --->8
# Jay shah
"""

# w+  : write + read  ----->new , exiting

"""with open("sujal.txt","w+") as f :
    f.write("my name is sujal sharma.\n")
    f.write("study  in INTERNATIONAL SCHOOL.\n")
    f.write("made in rajasthan.\n")
    f.seek(0)
    c=f.read()
    print(c)
    f.close()

"""

# exceptional  handling  :
"""
syntax : 

try : 
    code
except (error)
    print
finally
    print

"""
# ex :1 
"""try :
      a=int(input("enter a :"))
      b=int(input("enter b :"))
      print("div :",a/b)
except ZeroDivisionError :
    print("you can't divide by zero")
finally :
    print("done")
"""

# connectivity  with sql  : 
import mysql.connector 

conn = mysql.connector.connect(
    host="localhost",
    port = 3306,
    user="root",
    password="root",
    database="crud"
)
cursor= conn.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS crud")

# cursor.execute("CREATE TABLE IF NOT EXISTS student(id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(50),age INT,hobby VARCHAR(50))")

cursor.execute("INSERT INTO student(name,age,hobby) VALUES('tisha',22,'sleeping')")
cursor.execute("INSERT INTO student(name,age,hobby) VALUES('sujal',20,'power BI')")
cursor.execute("INSERT INTO student(name,age,hobby) VALUES('mayank',27,'late coming always')")
cursor.execute("INSERT INTO student(name,age,hobby) VALUES('vansh',22,'gamer-streamer')")

conn.commit()
print("table inserted")
cursor.close()
conn.close()


# fetch all ()