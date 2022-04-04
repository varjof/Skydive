# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 14:50:06 2020
@author: John
"""

import matplotlib.pyplot as plt

yo=3000 #Altura de lanzamiento
vo=0 #Vel inicial en dirección de y
k=0.5 #Cte de fricciónd el aire sin paracaidas
yp=1500 #apertura del paracaidas
m=7 #Masa del paracaidista
dt=1
g=9.8
t=0
y=yo
v=vo

bola,=plt.plot(0,yo,'o')
plt.axis([-1,1,0,3050])
plt.ylabel("y")
plt.xlabel("x")   
 
for i in range(200):
    t=t+dt
    v=(-g-k/m*v)*dt+v
    y=v*dt+y
    bola.set_ydata(y)
    if y<=1500:
        k=7
        bola.set_markersize(20)
        #plt.plot(0,y,'o')
    plt.pause(0.1)
