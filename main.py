'''
Author: Callum
Version: 1.0
Date: 28/06/2022

'''


'''
This Class is used to explain what sets are and types of sets
'''

import tkinter
from tkinter import *


class Sets:
    def whatIs(self):
        print('What are sets?')
        print("A Set is a collection of unique values")
    def whatIsAUnion(self):
        print("What is a union?")
        print("A union is the result of combining two sets")
    def whatIsAIntersection(self):
        print("What is an intersection?")
        print("A intersection is the result of combining two sets and removing the duplicates.")


'''
This Class is used to explain what algebra is and types of algebra
'''
class Algebra:
    def whatIs(self):
        print("What is algebra?")
        print("Algebra is the study of the properties of numbers and operations on numbers")

    def whatIsACoefficient(self):
        print("What is a coefficient?")
        print("A coefficient is the result of multiplying a number by a power of a base number")

    def whatIsAVariable(self):
        print("What is a variable?")
        print("A variable is a number that can be used in a mathematical expression")

    def whatIsAConstant(self):
        print("What is a constant?")
        print("A constant is a number that cannot be changed")

    def whatIsAReciprocalDetailed(self):
        print("What is a reciprocal?")
        print('The reciprocal of a number is the number that can be multiplied by it to equal the original number')

'''
This Class is used to explain what geometry is and types of geometry
'''
class Geometry:
    def whatIs(self):
        print("What is Geometry?")
        print("Geometry is the study of shapes and their properties")

    def whatIsaAAcuteangle(self):
        print("What is an acute angle?")
        print("An acute angle is an angle whose measure is less than 90 degrees")
    
    def whatIsAnObtuseangle(self):
        print("What is an obtuse angle?")
        print("An obtuse angle is an angle whose measure is greater than 90 degrees")
    
    def whatIsARightAngke(self):
        print("What is a right angle?")
        print("A right angle is an angle whose measure is 90 degrees")

'''
This Class is used to explain what trigonometry is and types of trigonometryno
'''
class Trigonometry:
    def whatIs(self):
        print("What is Trigonometry?")
        print("Trigonometry is the study of the properties of triangles")

    def whatIsASine(self):
        print("What is sine?")
        print("Sine is the measure of the angle between the sides of a triangle, and is the opposite side of the triangle from the hypotenuse")

    def whatIsACosine(self):
        print("What is cosine?")
        print("Cosine is the measure of the angle between the sides of a triangle, and is the adjacent side of the triangle from the hypotenuse")

    def whatIsATangent(self):
        print("What is tangent?")
        print("Tangent is the measure of the angle between the sides of a triangle, and is the opposite side of the triangle from the adjacent side")
    

'''
This Function is used to call the main function
It asks what you want to learn and calls the oop code from the above classes
'''
def main():
    print('What Do You Wanna Learn About')
    print('1. Sets')
    print('2. Algebra')
    print('3. Geometry')
    print('4. Trigonometry')
    print('5. Exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        sets = Sets()
        sets.whatIs()
        sets.whatIsAUnion()
        sets.whatIsAIntersection()
    elif choice == 2:
        algebra = Algebra()
        algebra.whatIs()
        algebra.whatIsACoefficient()
        algebra.whatIsAVariable()
        algebra.whatIsAConstant()
        algebra.whatIsAReciprocalDetailed()
    elif choice == 3:
        geometry = Geometry()
        geometry.whatIs()
        geometry.whatIsaAAcuteangle()
        geometry.whatIsAnObtuseangle()
        geometry.whatIsARightAngke()
    elif choice == 4:
        trigonometry = Trigonometry()
        trigonometry.whatIs()
        trigonometry.whatIsASine()
        trigonometry.whatIsACosine()
        trigonometry.whatIsATangent()
    elif choice == 5:
        print('Goodbye')
    else:
        print('Invalid Choice')
        main()



main()