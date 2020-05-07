# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:08:03 2020

@author: afern
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider


KT=2.5
def p1(c,E,c0):
	
	E=E*KT
	c=c*1e-6
	B=1/(KT)
	num=(c/c0)*np.exp(-B*E)
	Z=1+(c/c0)*np.exp(-B*E)
	return (num/Z)





fig,ax=plt.subplots()
plt.ylim(0,1)
plt.subplots_adjust(left=0.25,bottom=0.4)
c=np.arange(0,100,0.001)
ax.set_ylabel(r"$P_{union}$",fontsize=25)
ax.set_xlabel(r"$c(\mu M)$",fontsize=25)


#P1=p1(c,-10,1.8)
#l1,=ax.plot(c,P1,label=r"$C_0=5M$")
#P1=p1(c,-10,0.6)
#l2,=ax.plot(c,P1,label=r"$C_0=0.6M$",linewidth=3.3)
#P1=p1(c,-10,0.02)
#l2,=ax.plot(c,P1,label=r"$C_0=0.02M$",color="violet")
#P1=p1(c,-12.5,0.6)
#l1,=ax.plot(c,P1,label=r"$\Delta\epsilon_1 (k_B T)=-12.5$")
#P1=p1(c,-10,0.6)
#l2,=ax.plot(c,P1,label=r"$\Delta\epsilon_1 (k_B T)=-10$")
#P1=p1(c,-7.5,0.6)
#l3,=ax.plot(c,P1,label=r"$\Delta\epsilon_1 (k_B T)=-7.5$")



P1=p1(c,-10,1.8)
l1,=ax.plot(c,P1,label=r"$P_1$")
ax.legend(fontsize=15)
ax.margins(0) ##Hacce que la funcion se evalue sobre todo el eje
plt.show()	

axcolor= "lightgoldenrodyellow"
axE=plt.axes([0.25,0.1,0.65,0.03],facecolor=axcolor)
axC=plt.axes([0.25,0.2,0.65,0.03],facecolor=axcolor)

sE=Slider(axE,"E",-12.5,-5,valinit=-5)
sC=Slider(axC,"C",1e-10,1,valinit=0.6)

def update(val):
	E=sE.val
	C=sC.val
	l1.set_ydata(p1(c,E,C))
	fig.canvas.draw_idle()
	
sE.on_changed(update)
sC.on_changed(update)



