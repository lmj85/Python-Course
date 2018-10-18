#!/usr/bin/env python
# coding: utf-8

# In[1]:


y = int(input("If you want to convert C to F enter 1, if you want the opposite enter 2: "))
if y == 1:
    x = float(input("Enter the Temperature in Celsius: "))
    print("Temperature in Fahrenheir is: " , end = "")
    print(float( (x * 1.8) + 32))
elif y == 2:
    x = float(input("Enter the temperature in Fahrenheit: "))
    print("Temperature in Celsius is: ", end = "")
    print(float((x - 32)/1.8))


          


# In[ ]:




