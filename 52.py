# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 20:44:29 2017

@author: anju
"""

"""
Question: The code is supposed to ask the user to enter their name and 
surname and then it prints out those user submitted values. 
Instead, the code throws a TypeError. Please fix it so 
that the expected output is printed out.

firstname = input("Enter first name: ")
secondname = input("Enter second name: ")
print("Your first name is %s and your second name is %s" % firstname, secondname)
"""

firstname = input("Enter first name: ")
secondname = input("Enter second name: ")
print("Your first name is %s and your second name is %s" %(firstname, secondname))