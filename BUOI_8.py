import matplotlib.pyplot as plt
y1=[]
y2=[]
x = range(-100,100,10)
for i in x: y1.append(i**2)
for i in x: y2.append(-i**2)

plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel("x")
plt.xlabel("y")
plt.ylim(-2000,2000)
plt.axhline(0) # horizontal line
plt.axvline(0) # vertical line

plt.savefig("quad.png")
plt.show()