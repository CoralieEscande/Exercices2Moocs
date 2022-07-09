# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 12:22:42 2021

@author: Coralie
"""

from pyibex import *
from vibes import vibes
# define the function (x,y) -> sin(x+y)
f = Function('x', 'y', 'x*cos(x-y)+y')
# build the Forward / backward separator f(x,y) < 0
sep = SepFwdBwd(f, [-oo, 0])
# define the initial domain [-10,10]x[-10,10]
X0 = IntervalVector(2, [-10,10])
#initialize vibes display
vibes.beginDrawing()
# run the set inversion algorithm
pySIVIA(X0, sep, 0.1)
vibes.endDrawing()

