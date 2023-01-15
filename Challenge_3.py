# challenge 3
# In this challenge, you will implement a student class

# Solution 
class Student:

    def setName(self,x):
        self.__Name = x
    def getName(self):
        print('Name: ')
        return self.__Name
    def setRollNumber(self,y):
        self.__Rnumber = y
    def getRollNumber(self):
        print('Roll Number: ')
        return self.__Rnumber
        
A = Student()
A.setName('Edyoda')
A.setRollNumber('DS291122A')
print (A.getName())
print (A.getRollNumber())
