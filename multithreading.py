import threading
def print_Cube(num):
    print("Cube:{}".format(num*num*num))
def print_Square(num):
    print("Square:{}".format(num*num))
if __name__=="__main__":
    t1=threading.Thread(target=print_Square,args=(10,))
    t2=threading.Thread(target=print_Cube,args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done!!")
