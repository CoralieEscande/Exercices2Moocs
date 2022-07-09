from autolib import *  # available at https://www.ensta-bretagne.fr/jaulin/autolib.py
 

def lqr(A,B,Q,R):
    X = solve_continuous_are(A,B,Q,R)
    K = inv(R)@(B.T@X) 
    eigVals, eigVecs = eig(A-B*K) 
    print('eigVals',eigVals)
    print('\n K=',K)
    return K
    

def f(x,u):
    s,θ,ds,dθ=list(x[0:4,0])
    dds=(mr*sin(θ)*(g*cos(θ)- l*dθ**2) + u)/(mc+mr*sin(θ)**2)
    ddθ= (sin(θ)*((mr+mc)*g - mr*l*dθ**2*cos(θ)) + cos(θ)*u)/ (l*(mc+mr*sin(θ)**2))
    return(array([[ds],[dθ],[dds],[ddθ]]))
    
    


mc,l,g,mr=5,1,9.81,1
A = array([[0,0,1,0],[0,0,0,1],[0,mr*g/mc,0,0],[0,(mc+mr)*g/(mc*l),0,0]])
B = array([[0],[0],[1/mc],[1/(mc*l)]])


dt = 0.1
kmax=10
x = array([[2],[0],[0],[0]]) 
tmax=dt*kmax
ax=init_figure(-3,3,-3,3)

for k in range(0,kmax): 
    clear(ax)
    draw_invpend(ax,x,'blue')
    u = 0
    x = x + dt*f(x,u)  
pause(1) 
       

