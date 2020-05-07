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
	num=2*(c/c0)*np.exp(-B*E)
	Z=1+2*(c/c0)*np.exp(-B*E)+(c**2/c0**2)*np.exp(-B*(2*E+J))
	return (num/Z)

def p0(c,E,J,c0):
	
	E=KT*E
	J=J*KT
	B=1/(KT)
	num=1
	Z=1+2*(c/c0)*np.exp(-B*E)+(c**2/c0**2)*np.exp(-B*(2*E+J))
	return (num/Z)

def p2(c,E,J,c0):
	
	E=KT*E
	J=J*KT
	B=1/(KT)
	num=(c**2/c0**2)*np.exp(-B*(2*E+J))
	Z=1+2*(c/c0)*np.exp(-B*E)+(c**2/c0**2)*np.exp(-B*(2*E+J))
	return (num/Z)


c0=760
J=1
E=-5
fig,ax=plt.subplots()
plt.ylim(0,1)
plt.subplots_adjust(left=0.25,bottom=0.4)
c=np.arange(1e-2,1e3,0.005)
ax.set_ylabel(r"$P_{union} $", fontsize=25)
ax.set_xlabel("p(mmHg)",fontsize=25)


#P1=p1(c,E,J,c0)
#l1,=ax.plot(c,P1,label=r"$p_1$")
#plt.xscale("log")
#
#P2=p2(c,E,J,c0)
#l2,=ax.plot(c,P2,label=r"$p_2$")
#plt.xscale("log")
#
#P0=p0(c,E,J,c0)
#l0,=ax.plot(c,P0,label=r"$p_0$",color="violet")
#plt.xscale("log")
#ax.legend(fontsize=15)
#ax.margins(0) ##Hacce que la funcion se evalue sobre todo el eje
plt.show()	

axcolor= "lightgoldenrodyellow"
axE=plt.axes([0.25,0.1,0.65,0.03],facecolor=axcolor)
axJ=plt.axes([0.25,0.15,0.65,0.03],facecolor=axcolor)
axC=plt.axes([0.25,0.2,0.65,0.03],facecolor=axcolor)

sE=Slider(axE,"E",-6,4,valinit=-5)
sJ=Slider(axJ,"J",-10,10,valinit=-0.25)
sC=Slider(axC,"C",300,1000,valinit=760)

def update(val):
	J=sJ.val
	E=sE.val
	C=sC.val
	l1.set_ydata(p1(c,E,J,C))
	l2.set_ydata(p2(c,E,J,C))
	l0.set_ydata(p0(c,E,J,C))
	fig.canvas.draw_idle()
	
sJ.on_changed(update)
sE.on_changed(update)
sC.on_changed(update)



















