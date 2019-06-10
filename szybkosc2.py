#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 22:01:27 2019

@author: ignacy
"""

import cantera as ct
from sdtoolbox.postshock import CJspeed
from sdtoolbox.postshock import PostShock_eq
from sdtoolbox.thermo import soundspeed_eq, soundspeed_fr
import numpy as np
import matplotlib.pyplot as plt

P0 = 101325.0
T0 = 295

npoints = 20

q1 = 'H2:2 O2:1 N2:3.76'
q2 = 'H2:2 O2:1'


mech = 'gri30.xml'

# H2 + air
gas_initial1 = ct.Solution(mech)
gas_initial1.TPX = T0, P0, q1

#H2 + oxygen
gas_initial2 = ct.Solution(mech)
gas_initial2.TPX = T0, P0, q2



# compute CJ speed fo different prssures

speed1 = np.zeros(npoints)
speed2 = np.zeros(npoints)


P = np.linspace(0.1*ct.one_atm, ct.one_atm*3, npoints)

#H2 + air

for i in range(npoints):
    [cj_speed,R2,plot_data] = CJspeed(P[i], T0, q1, mech, fullOutput=True)  
    speed1[i] = cj_speed
    # print('At P = {0:12.4g}, V = {1:12.4g}'.format(P[i], speed[i]))

    
print('V(p) for H2-air mixture')
fig, ax = plt.subplots()
ax.plot(P/100000, speed1)
ax.set(xlabel='Pressure [bar]', ylabel='Detonation speed [m/s]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

#H2 + oxygen

for i in range(npoints):
    [cj_speed,R2,plot_data] = CJspeed(P[i], T0, q2, mech, fullOutput=True)  
    speed2[i] = cj_speed
    # print('At P = {0:12.4g}, V = {1:12.4g}'.format(P[i], speed[i]))

    
print('V(p) for H2-oxygen mixture')
fig, ax = plt.subplots()
ax.plot(P/100000, speed2)
ax.set(xlabel='Pressure [bar]', ylabel='Detonation speed [m/s]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()


# compute CJ speed fo different temperatures

speed4 = np.zeros(npoints)
speed5 = np.zeros(npoints)


T = np.linspace(273, 2000, npoints)

#H2 + air

for i in range(npoints):
    [cj_speed,R2,plot_data] = CJspeed(P0, T[i], q1, mech, fullOutput=True)  
    speed4[i] = cj_speed
    
print('V(T) for H2-air mixture')
fig, ax = plt.subplots()
ax.plot(T, speed4)
ax.set(xlabel='Temperature [T]', ylabel='Detonation speed [m/s]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

#H2 + oxygen

for i in range(npoints):
    [cj_speed,R2,plot_data] = CJspeed(P0, T[i], q2, mech, fullOutput=True)  
    speed5[i] = cj_speed
    
print('V(T) for H2-oxygen mixture')
fig, ax = plt.subplots()
ax.plot(T, speed5)
ax.set(xlabel='Temperature [T]', ylabel='Detonation speed [m/s]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

