#!/usr/bin/env python
# coding: utf-8

# In[6]:


x = float(input("Enter your number: "))
if x < -100:
    print(-x)
elif x >= -100 and x <= -25:
        print(x ** 4)
elif x > - 25 and x <= 0:
    print(3 * (x ** 2) - 1)
elif x > 0 and x <= 100:
    print((22/14 * x) + (3 ** x))
elif x > 100:
    print(x)
  # the best data type for f(x) is float  

