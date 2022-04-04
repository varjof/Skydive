# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 14:30:30 2020

@author: John
"""

import numpy as np
import matplotlib.pyplot as plt

yo=3000 #Altura de lanzamiento
vo=0 #Vel inicial en dirección de y
k=0.5 #Cte de fricciónd el aire sin paracaidas
yp=1500 #apertura del paracaidas
m=7 #Masa del paracaidista
dt=0.1
g=9.8
t=0
y=yo
v=vo

Ay=[y]
At=[t]
Av=[v]

for i in range(600):
    t=t+dt
    v=(-g-k/m*v)*dt+v
    y=v*dt+y
    Ay.append(y)
    At.append(t)
    Av.append(v)
    if y<=1500:
        k=7
       
plt.plot(At,Ay)
plt.xlabel("t")
plt.ylabel("y")

plt.figure(2)    
plt.plot(At,Av)
plt.xlabel("t")
plt.ylabel("v")
