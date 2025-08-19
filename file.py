f=open("demo.txt","r")
print(f.read())
print(f.read(1))
print(f.readline())
for i in f:
    print(f.read())
f.close()    
