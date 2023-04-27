#!/usr/bin/env python
# coding: utf-8

#  Break :
#  
#   1 ‘Break’ in Python is a loop control statement. 
#   2 It is used to control the sequence of the loop.
#   3 Suppose you want to terminate a loop and skip to the next code after the loop; break will help you do that. 
#   4 A typical scenario of using the Break in Python is when an external condition triggers the loop’s termination. 
#   
#   The syntax is as follows:
# 
#    break;
# 
#   It is used after the loop statements.
# 
# Nested Loops In Python :
#   1.When working with nested loops, the break statement can be used to break out of both the inner and outer loops.
#   2.If a break statement is encountered in the inner loop, only the inner loop will be exited and the outer loop will continue    to iterate.
# 

# In[15]:


l1=[4,3,7,5]
l2=[12,14,16,18]

for i in l1:
    for j in l2:
        print(i,j)
        if i==7 and j==12:
            print('break')
            break
                
                
               


# In[ ]:




