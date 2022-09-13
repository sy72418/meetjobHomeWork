# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 11:00:17 2022

@author: user
"""

# 費式數列 Q1
print('Q1.')
num = [1,1]
x=0
y=1
while len(num)<25:
    z=num[x]+num[y]
    num.append(z)
    x+=1
    y+=1

print('費式數列前25項之和：',sum(num))
print('-'*30)

#費式數列 Q2
print('Q2.')
num1 = [1,2]
x=0
y=1
for i in range(1,26):
    print(num1[y],'/',num1[x],end=',')
    z=num1[x]+num1[y]
    num1.append(z)
    x+=1
    y+=1
print()
print('-'*30)

#有空題
print('Q3.')
a = 1
n = 1
for x in range(5):
    for y in range(a):
        print(n,end=' ')
        n+=1
    print()
    a+=1
        
       



