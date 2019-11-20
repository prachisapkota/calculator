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
f1.close()'''



