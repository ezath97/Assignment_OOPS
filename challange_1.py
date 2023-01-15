#Challenge 1: Square Numbers and Return Their Sum
#Task 1: 👉 Implement a constructor to initialize the values of three properties: x, y, and z.
#Task 2: 👉 Implement a method, sqSum(), in the Point class which squares x, y, and z and returns their sum.
#Sample properties 1, 3, 5
#Sample method output 35

#Solution
class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        print("Sample method output: ", self.x**2 + self.y**2 + self.z**2)
        
X = Point(1,3,5)
(X.sqSum())