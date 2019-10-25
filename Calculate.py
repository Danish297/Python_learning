#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Below are few maths funciton can be used in anyother programme.


# In[1]:


def add_num(*numbers):
    total = 0
    for num in numbers:
        total += num
    print(f"\n The total of givne numbers is:: {total}")
    
def multiply_num(*numbers):
    total = 1
    for num in numbers:
        total *= num
    print (f"\n The total multiplication of givne number is:: {total}")
    
def subtract_num(num1,num2):
    print(f"\n After subtraction from {num1} to {num2} is {num1-num2}")
    
def division_num(num1,num2):
    print(f"\n Result of division is:: {num1/num2}")


# In[ ]:




