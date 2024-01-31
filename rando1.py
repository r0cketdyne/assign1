# Program 1 -- File: Program1.py
# MATTHEW STEPHENSON 1/14/2024
# This program computes the volume of a cone
###########################################################
import math
#we will first import the math lib to access
#the mathematical functions necesarry to perform computations
#related to the volume of a cone.
radius = float(input("Enter the radius of the cone in cm: "))
#radius data was input via user as a string and immediately
#converted to a float using a build in python function in-line
#this was then assigned to a specific address at memory
height = float(input("Enter the height of the cone in cm: "))
#height data was input via user as a string and immediately
#converted to a float using a built in python function in-line
#this was then assigned to a specific address at memory.
volume = math.pi * radius**2 * height / 3
#volume is set to a specific location at memory at the stack
#the math.pi function from standard math lib imported above
#is used to access the value of pi. computation is
#performed using the formula for the volume of a cone
#supplied at program1 documentation at canvas
ounces = volume * 0.033814
#to get 0.33814 I computed 1/29.5735296 which was derived from 
#the fact that there
#are 29.5735296 milliliters per ounce.
#if you multiply volume by 0.33814, the resulting value is the #volume at ounces.
print("Cone volume was computed to be", volume, "cm cubed")
#volume address at memory with computed data was logged to the #terminal emulator
#at the standard input / output.
print("Which is equivalent to", ounces, "oz.")
#ounces address at memory with computed data from the volume address at memory was
#logged to the terminal emulator for viewing at the standard input / output.
print("Program 1 terminated. Au revoir!")
#program termination message logged to terminal emulator at #the standard input /
output.
