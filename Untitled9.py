#!/usr/bin/env python
# coding: utf-8

# In[8]:


with open('bookstore (1).xml') as f:
    for line in f:
        print(line.strip())


# In[9]:


import xml.etree.ElementTree as ET
tree=ET.parse("bookstore (1).xml")
root=tree.getroot()
print(root.tag)


# In[10]:


for child in root:
    print(child.tag, child.attrib)


# In[14]:


print(root[1][0].text)


# In[15]:


for title in root.iter('title'):
    print(title.attrib)


# In[16]:


file=open("rahma.txt","w")
file.write(" bookstore ")
file.close()


# In[18]:


f = open("rahma.txt", "r")  
print(f.read())   
f.close()   


# In[19]:


file = open("rahma.bin", "wb")

file.write(b"This binary string will be written to rahma.bin")

file.close()


# In[20]:


file = open("rahma.bin", "rb")

print(file.read())

file.close()


# In[21]:


file = open("rahma.bin", "rb")

print(file.read(4))

file.close()


# In[22]:


file=open("array.bin","wb")
num=[1,2,3,4,5,6]
array=bytearray(num)
file.write(array)
file.close()


# In[24]:


file=open("array.bin","rb")
num= list(file.read())
print(num)
file.close()


# In[ ]:




