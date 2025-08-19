def fun1(k):
    if(k>0):
        print("k value ::",k)
        result=k+fun1(k-1)
        print("check",k-1)
        print("If",result)
    else:
        result=0
    return result
print("Recursion Example")
fun1(3)        
