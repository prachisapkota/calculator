#write
'''f=open('File.txt', 'w')
f.writelines("this is my \n first file")
f.close()
with open("File.txt", 'r') as f:
    text=f.read()
print(text)
f=open('File.txt', 'a')
f.writelines(" append text")
f.close()
with open("File.txt", 'r') as f:
    text=f.read()
print(text)

f1=open("file1.txt", 'w')
text=input("write to the file.....write quit to stop ")
while text!='quit':
    f1.writelines(text+ '\n')
    text=input()
print("done with writing")
f.close()

#creating file which support user entry

file=open("file.txt",'w')
text=input("Write to the file and type '////' to exit")
while text!='////':
    file.writelines(text+'\n')
    text=input()
print("Done with writing")
file.close()

 #HOMEWORK
#to replace string and save as new file
file=open("File1.txt",'r+')
file.writelines("Hello-this-is-a-text-file")
text1=file.readline()
print (text1)
text2=text1.replace('-',' ')
print(text2)
file.close()

#prime number using list comprehension
list=[x for x in range(2,2500) if all (x % y !=0 for y in range(2,x))]
print(list)

#map function to convert list in farenheit to list in temperature
list_f= [20, 50, 56, 98.9, 98.8]
list_c= list(map(lambda x:((x-32)/1.8), list_f))
print(list_c)

#copy a text from one file to another
file=open("file5.txt",'w')
file.writelines("Hello Python!!\t")
file.close()
with open("file5.txt", 'r') as file:
    txt=file.read()
    print(txt)
    file.close()

f1=open("new.txt",'a')
f1.writelines(txt)
f1.close()

class LowLengthError(Exception):
    def __init__(self):
        super(LowLengthError, self).__init__("String length must be greater than 3. ")

string = str(input("Enter any string....  "))
if len(string)<3:
    raise LowLengthError
else:
    print("Accepted")

a = int(input("Enter the first number\t"))
b = int(input("Enter the second number\t"))
div = a / b
print(div)
except ZeroDivisionError:
    print("You cannot have division by zero.")
except:
    print("Some error has occurred, check it again")

#CLASS8
# Using the OS library change the name of a file.

import os
os.rename(r'C:\november11\prachi.txt',r'C:\november11\rename.txt')

# Using Print the current weekday, day, month  and year in separate statements.

import datetime as dt
print(dt.date.today(),'\n')
print("year:",dt.date.today().year,)
print("month:",dt.date.today().month,)
print("day:", dt.date.today().day)
print("Week:",dt.date.today().weekday(),'\n')'''

# Use two functions in the math library.
import math
print("The square root of 5 is\t", math.sqrt(5))
print("The value of cosine 30 is", math.cos(30))



