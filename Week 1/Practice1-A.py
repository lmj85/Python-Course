#!/usr/bin/env python
# coding: utf-8

# In[7]:


A = input("Enter you name: ")
x = input("Enter the first number: ")
y = input("Enter the second number: ")
print("Hi Mr/Mrs." + A + ",")
print(f"The Sum of {x} and {y} is: ", end = "")
print(float(x) + float(y))
print(f"The Sub of {x} and {y} is: ", end = "")
print(float(x) - float(y))
print(f"The Mul of {x} and {y} is: ", end = "")
print(float(x) * float(y))
print(f"The Div of {x} over {y} is: ", end = "")
print(float(x) / float(y))
print(f"The Reminder of {x} over {y} is: ", end = "")
print(float(x) % float(y))
print(f"The Exponent of {x} to the power of {y} is: ", end = "")
print(float(x) ** float(y))


