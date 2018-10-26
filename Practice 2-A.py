#!/usr/bin/env python
# coding: utf-8

# In[1]:


def print_prime_numbers(n):
    prime = []
    count = 1
    while True: 
        if count % 2 == 0 or count % 3 == 0 or count % 5 == 0:
            count += 1
        
        else:
            prime.append(count)
            count += 1
            if len(prime) == n:
                break
                
    print(prime)


# In[2]:


print_prime_numbers(15)

