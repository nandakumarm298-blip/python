file=open("example.txt","w")
file.write("hello this is first line/n")
file.write("This is second line")
file.close()

file=open("example.txt","r")
for i in file:
    print(file.read(1))
file.close()    
