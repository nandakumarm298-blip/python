import matplotlib.pyplot as plt  
import numpy as np

xp=np.array([0,6])
yp=np.array([0,50])
plt.plot(xp,yp)
plt.show()

xp=np.array([5,6])
yp=np.array([1,40])
plt.plot(xp,yp,'o')
plt.show()

x=np.array([1,2,6,8])
y=np.array([3,8,1,10])
print(x,y)
plt.plot(x,y,'o')
plt.show()

y=np.array([3,8,1,10])
plt.plot(y,marker='H')
plt.show()

y=np.array([3,8,1,10])
plt.plot(y,'o:r')
plt.show()

x=[10,20,30,40,50]
y=[60,70,80,90,100]
plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()
plt.show()

plt.plot([1,2,3,4])
plt.plot([10,20,30,40])
plt.plot([1,2,3,4,5],[10,20,30,40,50])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

x=[10,20,30,40]
plt.plot(x,x,'ro')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xlim(0,50)
plt.ylim(0,45)
plt.plot(x)
plt.grid(True)
plt.show()

t1=np.arange(5)
plt.plot(t1,'r--',t1**2,'bs',t1**3,'g^',t1**4,'ro')
plt.show()

x=[1,2,3,4]
plt.plot(x,[elem for elem in x],label='linear')
plt.plot(x,[elem**2 for elem in x],label='square')
plt.grid(True)
plt.legend()
plt.savefig('fig.png')
plt.show()

#Histogram
data=np.random.randn(8,8)
plt.hist(data)
plt.show()

x=[10,20,30]
plt.hist(x)
plt.show()

x=[10000,20000,3000,40000,50000]
my_label=['HERO','HONDA','PULSAR','ROYAL ENFILD','KTM']
plt.pie(x,labels=my_label)
plt.show()

#Scatter plot
x=np.random.rand(100)
y=np.random.rand(100)
plt.scatter(x,y)
plt.show()
