import math

x=int(input("Number of sides:"))
y=int(input("Size of sides:"))
z=((x*y**2))/(4*math.tan(math.pi/x))
print(int(z))