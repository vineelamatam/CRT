'''
Debugging in python:
bug --> error
finding and fixing errors-->debugging
Types of errors:
1. syntax errors --> missing of colon, or intendation
2. runtime errors --> division by zero
3. logical errors --> missing of logic

Debugging techniques:
1.print statements debgging
2.try-except
3.using pdb
    pdb-->python Debugger purpose
    1. pause the execution code
    2. try-execpt
    3. To run the code line by line
pdp commands:
1.n --> to excute the output in a next line
2.p variable --> to get the the value of a variable 
3.l --> list nearby code
4.c --> continue the execution
5.s --> to start a function
6.r --> return from the function 
7.h --> help
8.q --> quit the  execution 

try:
    a=int(input("enter a number:"))
    print(10/a)
except ZeroDivisionError:
    print("can not divisible by Zero.")
except ValueError:
    print("Invalid input")
'''
import pdb

def add(a,b):
    pdb. set_trace()#set the breakpoint
    return a+b
a=int(input("Enter first  number:"))
b= int(input("Enter second  number:"))
print(add(a,b))
