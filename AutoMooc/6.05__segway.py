from autolib import *    # available at https://www.ensta-bretagne.fr/jaulin/autolib.py
m,M,l,g,ρ,Jp=10,1,1,10,1,10
Jm=(1/2)*M*ρ**2
μ1,μ2,μ3,μg=Jm+ρ**2*(m+M),Jp+m*l**2,ρ*m*l,g*l*m
dt=0.01

def f(x,u):
    s,θ,ds,dθ=list(x[0:4,0])
    den=(μ1*μ2-μ3**2*cos(θ)**2)
    dds = (μ3*(μ2*dθ**2-μg*cos(θ))*sin(θ)+(μ2+μ3*cos(θ))*u)/den
    ddθ = ((μ1*μg-μ3**2*dθ**2*cos(θ))*sin(θ)-(μ1+μ3*cos(θ))*u)/den
    return array([[ds],[dθ],[dds],[ddθ]])


ax = init_figure(-10,10, -10,10)
x=array([[0], [0.5], [0], [0]])
for t in arange(0,10,dt) :
    u=0
    x=x+dt*f(x,u)
    clear(ax)
    draw_segway(ax,x,'black',1)  
pause(3)

