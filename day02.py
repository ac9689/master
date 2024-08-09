'''p=("ashwani chauhan, \n\t john drew,\n john")
print(p)

#print python version
import sys
print("python version")
print(sys.version)
print("version info.")
print(sys.version_info)

#print time
import time
now=time
print(now.strftime("%H:%M:%S"))
#print date and time
import datetime
now=datetime.datetime.now()
print(now.strftime("%y-%m-%d \n%H:%M:%S"))
#ara of circle
from math import pi
r=int(input("enter the radious = "))
area=pi*r ** 2
print("Area of circle is= ",+ area)'''

#print first and last name from formatted string
a = input("Enter the first name: ")
#b = input("Enter the last name: ")
#c = f"My name is {a} {b}"
#print(c)
list=a.split(",")
print(list)
