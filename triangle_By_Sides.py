"""
 Triangular By Sides
 By: M.Yekmaz
 Date: 1400/07/10
"""

x=int(input("Please Enter first side: "))
y=int(input("Please Enter second side: "))
z=int(input("Please Enter third side(hypotenuse): "))

if x<y+z and y<x+z and z<x+y:
    if x==y==z:
        type="equilateral"
    elif x==y or y==z or x==z:
        type="isoceles"
    elif x**2+y**2==z**2:
        type="right"
    else:
        type="scalene"
    print(f"These 3 edges can make a {type} triangle")
else:
    print("These 3 edge can`t make a triangle")
