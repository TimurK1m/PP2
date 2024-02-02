import  math
class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("String in upper case:", self.input_string.upper())

manipulator = StringManipulator()
manipulator.getString()
manipulator.printString()


class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,lenght):
        super().__init__()
        self.lenght=lenght

    def area(self):
        return self.lenght*self.lenght

shape=Shape()
print(shape.area())
square=Square(5)
print(square.area())



class Rectangle(Shape):
    def __init__(self,):
        super().__init__()
        self.lenght=int(input("Lenght:"))
        self.wide=int(input("Wide:"))
    def area(self):
    
        return self.lenght*self.wide

rec=Rectangle(5,10)
print(rec.area())


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")
    
    def move(self,new_x,new_y):
        self.x=new_x
        self.y=new_y

    def dist(self,second_point):
        dx=self.x-second_point.x
        dy=self.y-second_point.y
        dist=math.sqrt(dx**2+dy**2)
        return dist
    
point1 = Point(2, 3)
point2 = Point(5, 7)

print("Initial Position:")
point1.show()
point2.show()

point1.move(4, 6)
point2.move(1, 2)
print("\nNew Position after Move:")
point1.show()
point2.show()

distance = point1.dist(point2)
print(f"\nDistance between the two points: {distance}")


class Bank:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def diposit(self,amount):
        self.balance+=amount
        print(f"На балансе:{self.balance}")

    def withdrawal(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Отаток{self.balance}")
        else:
            print("Ty Bomzh")



user=Bank("Ilya",0)

user.diposit(200)

user.diposit(700)


user.withdrawal(500)



def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [2, 3, 5, 7, 10, 13, 17, 20, 23, 29]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))