#!/usr/bin/env python
# coding: utf-8

# In[19]:


print(f'{"hello "}{"there, have fun"}{" ~ Aleksandra Mulewicz"}')


# In[5]:


#list of every character in upper and lower
chars = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']
filename = input("enter path: ") #path needs to be without quotation marks - getting to know it was painful, also / instead of \
f = open(filename, "r") #I succeed with storing variable, impossible
key = int(input("enter a key: "))

message = f.read()
def encode(message, key):
    enc_chars = str.maketrans( #this function replaces two strings, it will make representation 1:1
        f'{chars[0]}{chars[1]}', #here we're making one big string with both chars
        f'{chars[0][key:]}{chars[0][:key]}{chars[1][key:]}{chars[1][:key]}' #here we're making new alphabet which starts at the key char for example c if key == 3 and we're doing it analogically with upper letter alphabet
    )
    return str.translate(message, enc_chars) #having two alphabets: one normal, second encrypted, we can switch letters to make cipher
d = encode(message, key) 
print(d)

def decode(message, key):
    dec_chars = str.maketrans( #this function replaces two strings
        f'{chars[0][key:]}{chars[0][:key]}{chars[1][key:]}{chars[1][:key]}',
        f'{chars[0]}{chars[1]}'
    )
    return str.translate(message, dec_chars)
print(decode(d,key))


# In[7]:


g = "hey"

g[1:]


# In[8]:


f'{chars[0][key:]}{chars[0][:key]}{chars[1][key:]}{chars[1][:key]}'


# In[ ]:




