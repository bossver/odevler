#!/usr/bin/env python
# coding: utf-8

# In[2]:


import scipy as sc
import numpy as np
array1 = np.array ([(1,2,3)])
print (array1)


# In[3]:


array2=np.linspace(0,10,5)
print (array2 ,'\n')
array22=np.linspace(1,2,3)
print (array22,'\n')


# In[4]:


array3=np.arange(0,10,1)
print(array3,'\n')
array4 =np.arange(0.5,0.5)
print(array4,'\n')
array44=np.arange(5)
print(array44,'\n')
print (np.arange(10),'\n')


# In[5]:


array5=np.zeros(5)
print (array5,'\n')
array6=np.ones(3)
print(array6,'\n')


# In[6]:


array7=np.linspace(-2,3,6)
print (array7,'\n')
print (array7+2,'\n')
print (array7-1,'\n')
print (array7*3,'\n')
print (array7/2,'\n')
print (array7**4,'\n')
print((array7+2)*5,'\n')
print (np.sin(array7),'\n')
print (np.cos(array7),'\n')


# In[7]:


array8=np.array([10,20,30])
array9=np.array([50,60,70])
result1=array8+array9
print (result1,'\n')
print (array9-array8,'\n')
print (array8-array9,'\n')
print (array8*array9,'\n')
print (array9/array8,'\n')


# In[8]:


array10=np.array([[1,2,3],[4,5,6]])
print(array10,'\n')
array11=np.array([[1,1,1],[2,2,2],[3,3,3]])
print (array11,'\n')


# In[9]:


array12=np.array([np.eye(3)])
print (array12,'\n')


# In[19]:


array13=np.arange(8)
print(array13,'\n')
array14=np.reshape(array13,(2,4))
print(array14,'\n')
print(np.reshape(array13,(4,2),'\n')
print(np.reshape(np.arange(8),(4,2)),'\n')
print(np.reshape(array13,(2,5)),'\n')
      
      


# In[21]:


array15=np.array([[1,4,5],[2,3,6]])

print(array15,'\n')
print(array15+2,'\n')
print(array15-3,'\n')
print(array15*5,'\n')
print(2/array15,'\n')
print(array15**3,'\n')
print(np.cos(array15),'\n')


# In[23]:


array16=np.array([[1.,2.,3.,],[4.,5.,6.,]])
print(array16,'\n')
array17=np.array([[-1.,-2.,-3.,],[-4.,-5.,-6.,]])
print(array17,'\n')
array16*array17
print(np.dot(array16,array17),'\n')


# In[24]:


array18=sc.rand(8)
print(np.array(np.reshape((array18),(2,4))),'\n')
array19=print(np.array(np.reshape((sc.rand(8)),(2,4))),'\n')


# In[26]:


array20=np.array([[1,2,3],[4,5,6],[7,8,9,]])
print(array20[0,:],'\n')
print(array20[1,:],'\n')
print(array20[2,:],'\n')


# In[28]:


print(array20[:,0],'\n')
print(array20[:,1],'\n')
print(array20[:,2],'\n')


# In[30]:


print(array20[0,:]*array20[:,0],'\n')
print(array20[:,0]*array20[0,:],'\n')
print(np.dot((array20[0,:]),(array20[:,0])),'\n')
print(np.dot((array20[0,:]),np.array(np.reshape(array20[:,0],(3,1)))),'\n')
print(array20,'\n')
print(array20*array20,'\n')
print(np.dot(array20,array20),'\n')



# In[ ]:




