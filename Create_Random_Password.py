#!/usr/bin/python

from random import randint 

def generare_random_password(length=8):    
 password=" "
 for _ in range(length):
   password += chr(randint(40 , 130))
 return password
 
 
print(generare_random_password())
