def product(items):
    products=[]
    print(items)
    for i in items:
        products.append(i**2)
    return products
     #print(products)
my1=[10,20,30]
#product(my1)
my_result=product(my1)
print("Your productId is::",my_result)
