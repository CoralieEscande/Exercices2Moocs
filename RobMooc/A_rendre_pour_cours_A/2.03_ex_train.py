#! /usr/bin/env python3
# coding: utf-8
from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

def f(x,u):
    xr,yr,θr,vr = x.flatten()
    u1,u2 = u.flatten()
    return (array([[vr*cos(θr)],
                   [vr*sin(θr)],
                   [u1],
                   [u2]]))
def control(xr, wr, dwr, ddwr):
    xr,yr,θr,vr = xr.flatten()
    Ar = array([[-vr*sin(θr), cos(θr)],
               [vr*cos(θr), sin(θr)]])
    yr = array([[xr], [yr]])
    dyr = array([[vr*cos(θr)], [vr*sin(θr)]])
    v = (wr-yr) + 2 * (dwr-dyr) + ddwr
    ur = inv(Ar) @ v
    return ur


ax=init_figure(-30,30,-30,30)

dt = 0.1

xa = array([[10],[0],[1],[1]])
ua = array([[0],[0]])

xb = array([[10],[10],[13],[2]])
ub = array([[0],[0]])

xc = array([[0],[10],[1],[4]])
uc = array([[0],[0]])

xd = array([[20],[2],[2],[2]])
ud = array([[0],[0]])

xe = array([[-20],[-2],[5],[0.5]])
ue = array([[0],[0]])

omega = 0.1
Lx = 15
Ly = 7
l = 6
td = 1
te = 2

s = arange(0, 2*pi, 0.01)
p = array([Lx * cos(s),
          Ly * sin(s)])

for t in arange(0,50,dt) :    
    wa = array([[Lx * sin(omega * t)],
                [Ly * cos(omega * t)]])
    dwa = array([[Lx * omega * cos(omega * t)],
                 [- Ly * omega * sin(omega * t)]])
    ddwa = array([[0],
                  [0]])

    wb = array([[xa[0,0] - l * cos(xa[2,0])],
                [xa[1,0] - l * sin(xa[2,0])]])
    dwb = array([[xa[3,0] * cos(xa[2,0]) + l * ua[1,0] * sin(xa[2,0])],
                 [xa[3,0] * sin(xa[2,0]) - l * ua[1,0] * cos(xa[2,0])]])
    ddwb = array([[0],
                  [0]])

    wc = array([[xb[0,0] - l * cos(xb[2,0])],
                [xb[1,0] - l * sin(xb[2,0])]])
    dwc = array([[xb[3,0] * cos(xb[2,0]) + l * ub[1,0] * sin(xb[2,0])],
                 [xb[3,0] * sin(xb[2,0]) - l * ub[1,0] * cos(xb[2,0])]])
    ddwc = array([[0],
                  [0]])

    wd = array([[Lx * sin(omega * t - td)],
                [Ly * cos(omega * t - td)]])
    dwd = array([[Lx * omega * cos(omega * t - td)],
                 [- Ly * omega * sin(omega * t - td)]])
    ddwd = array([[0],
                  [0]])

    we = array([[Lx * sin(omega * t - te)],
                [Ly * cos(omega * t - te)]])
    dwe = array([[Lx * omega * cos(omega * t - te)],
                 [- Ly * omega * sin(omega * t - te)]])
    ddwe = array([[0],
                  [0]])

    clear(ax)
    plot2D(p,col='m',w=1)
    
    plot(wa[0], wa[1], 'ro', 1)
    plot(wb[0], wb[1], 'bo', 1)
    plot(wc[0], wc[1], 'go', 1)

    plot(wd[0], wd[1], 'yx', 1)
    plot(we[0], we[1], 'cx', 1)
    
    draw_tank(xa,col='red',r=1,w=2)
    draw_tank(xb,col='blue',r=1,w=2)
    draw_tank(xc,col='green',r=1,w=2)
    
    draw_tank(xd,col='y--',r=1,w=2)
    draw_tank(xe,col='c--',r=1,w=2)
    
    ua = control(xa, wa, dwa, ddwa)
    ub = control(xb, wb, dwb, ddwb)
    uc = control(xc, wc, dwc, ddwc)

    ud = control(xd, wd, dwd, ddwd)
    ue = control(xe, we, dwe, ddwe)
    
    xa = xa + dt * f(xa,ua)
    xb = xb + dt * f(xb,ub)
    xc = xc + dt * f(xc,uc)

    xd = xd + dt * f(xd,ud)
    xe = xe + dt * f(xe,ue)
#pause(1)

