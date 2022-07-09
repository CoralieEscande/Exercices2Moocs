#! /usr/bin/env python3
# coding: utf-8
from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

def draw(ap,aw): 
    aw=-aw-ap;
    c=2*array([-sin(ap),cos(ap)])
    plot( [0,c[0]],[0,c[1]],'magenta', linewidth = 2)
    for i in arange(0,8):
        plot(c[0]+array([0,cos(aw+i*pi/4)]),c[1]+array([0,sin(aw+i*pi/4)]),'blue')
    #pause(0.01)

def draw2(ap,aw): 
    aw=-aw-ap;
    c=2*array([-sin(ap),cos(ap)])
    plot( [0,c[0]],[0,c[1]],'red', linewidth = 2)
    for i in arange(0,8):
        plot(c[0]+array([0,cos(aw+i*pi/4)]),c[1]+array([0,sin(aw+i*pi/4)]),'green')
    #pause(0.01)
    

def f(x,u): 
    x=x.flatten()
    return array([[x[1]],[a*sin(x[0])-b*u],[-a*sin(x[0])+c*u]])

def controlk3(x, w, dw, ddw, dddw):
    x=x.flatten()
    eta = a * (c-b)
    ax = -b * eta * cos(x[0])
    bx = eta * sin(x[0]) * (a * cos(x[0]) - x[1]**2)
    y = c * x[1] + b * x[2]
    dy = eta * sin(x[0])
    ddy = eta * x[1] * cos(x[0])
    v = w - y + 3*(dw-dy) + 3*(ddw-ddy) + dddw
    u = (v-bx)/ax
    return u

def controlk2(x_bis, w_bis, dw_bis, ddw_bis):
    x = x_bis.flatten()
    y = x[0]
    dy = x[1]
    v = w_bis - y + 2*(dw_bis-dy) + ddw_bis
    u = (a*sin(x[0]) - v) / b
    return u

a,b,c = 10,1,2
dt = 0.1
x = array([[1],[0],[1]])
x_bis = array([[1],[0],[1]])
aw = 0  # wheel angle
aw_bis = 0
ax = init_figure(-3,3,-3,3)
for t in arange(0,15,dt) :
    #u=0
    
    w = 0
    dw = 0
    ddw = 0
    dddw = 0
    u = controlk3(x, w, dw, ddw, dddw)
    x = x + f(x,u)*dt
    aw = aw + dt*x[2]

    w_bis = 0
    dw_bis = 0
    ddw_bis = 0
    dddw_bis = 0
    u_bis = controlk2(x_bis, w_bis, dw_bis, ddw_bis)
    x_bis = x_bis + f(x_bis,u_bis)*dt
    aw_bis = aw_bis + dt*x_bis[2]
    
    clear(ax)
    draw(x[0],aw)
    draw2(x_bis[0],aw_bis)

 


