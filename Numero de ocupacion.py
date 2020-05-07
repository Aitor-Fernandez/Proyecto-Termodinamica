# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:17:20 2020

@author: afern
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 00:45:29 2020

@author: afern
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider


KT=2.5
def p1(c,E,J,c0):
	
	E=KT*E
	J=J*KT
	B=1/(KT)
	num=2*(c/c0)*np.exp(-B*E)+2*(c**2/c0**2)*np.exp(-B*(2*E+J))
	Z=1+2*(c/c0)*np.exp(-B*E)+(c**2/c0**2)*np.exp(-B*(2*E+J))
	return (num/Z)


c0=760
J=3
E=-5
fig,ax=plt.subplots()
plt.ylim(0,2)
plt.subplots_adjust(left=0.25,bottom=0.4)
c=np.arange(1e-2,5e3,0.005)
ax.set_ylabel(r"$<N_{un}>$", fontsize=25)
ax.set_xlabel("p(mmHg)",fontsize=25)


#P1=p1(c,E,-2.5,c0)
#l1,=ax.plot(c,P1,label=r"$J(K_BT)=-2.5$",linewidth=3.3)
#plt.xscale("log")
#
#P1=p1(c,E,0,c0)
#l2,=ax.plot(c,P1,label=r"$J(K_BT)=0$",color="violet")
#plt.xscale("log")
#
#P1=p1(c,E,5,c0)
#l2,=ax.plot(c,P1,label=r"$J(K_BT)=5$")
#plt.xscale("log")

ax.legend(fontsize=15)
ax.margins(0) ##Hacce que la funcion se evalue sobre todo el eje
plt.show()	

axcolor= "lightgoldenrodyellow"
axE=plt.axes([0.25,0.1,0.65,0.03],facecolor=axcolor)
axJ=plt.axes([0.25,0.15,0.65,0.03],facecolor=axcolor)
axC=plt.axes([0.25,0.2,0.65,0.03],facecolor=axcolor)

sE=Slider(axE,"E",-6,-4,valinit=-5)
sJ=Slider(axJ,"J",-10,10,valinit=-0.25)
sC=Slider(axC,"C",300,1000,valinit=760)

def update(val):
	J=sJ.val
	E=sE.val
	C=sC.val
	l1.set_ydata(p1(c,E,J,C))
	fig.canvas.draw_idle()

sJ.on_changed(update)	
sE.on_changed(update)
sC.on_changed(update)

	