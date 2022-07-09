from autolib import *  # available at https://www.ensta-bretagne.fr/jaulin/autolib.py

       
def draw_pend(x,col): 
    θ=x[0,0]
    plot([0,-sin(θ)],[0,-cos(θ)],col, linewidth = 2)    

s=2   
x=array([[1],[2]])
ax=init_figure(-s,s,-s,s)
draw_pend(x,'red')    
pause(1)
    
    



