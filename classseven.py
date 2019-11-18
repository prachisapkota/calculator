#write
f=open('File.txt', 'w')
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