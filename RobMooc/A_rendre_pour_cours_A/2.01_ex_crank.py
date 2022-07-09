#! /usr/bin/env python3
# coding: utf-8
from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

def draw_crank(y,z): 
    clear(ax)
    plot( [0,z[0,0],y[0,0]],[0,z[1,0],y[1,0]],'magenta', linewidth = 2)
    draw_disk(c,r,ax,"cyan")

def pos_calc(x):
    θ1=x[0,0]
    θ2=x[1,0]
    z=L1*array([[cos(θ1)],[sin(θ1)]])
    y=z+L2*array([[cos(θ1+θ2)],[sin(θ1+θ2)]])
    return y,z

def f(x, t, y, z):
    θ1=x[0,0]
    θ2=x[1,0]
    """ consigne statique"""
    #dθ1=1
    #dθ2=2
    """ consigne dynamique : suivi d'un cercle"""
    w = c + r * array([[cos(t)],[sin(t)]])
    plot(w[0,0], w[1,0], 'ro', linewidth = 2)
    dw = r * array([[-sin(t)],[cos(t)]])
    v = w - y + dw
    A = array([[-y[1,0], -L2*sin(θ1+θ2)], [y[0,0], L2*cos(θ1+θ2)]])
    u = inv(A) @ v
    return u
    #return(array([[dθ1],[dθ2]]))

def main():
  x = array([[-1],[1]])

  for t in arange(0,10,dt) :
    y, z = pos_calc(x)
    draw_crank(y,z)
    x = x + dt*f(x, t, y, z)

if __name__ == "__main__":
  """Définition des constantes"""
  L1,L2 = 4,3
  c = array([[1],[2]])
  r=4
  dt = 0.05
  ax=init_figure(-8,8,-8,8)
  """ Simulation """
  main()

