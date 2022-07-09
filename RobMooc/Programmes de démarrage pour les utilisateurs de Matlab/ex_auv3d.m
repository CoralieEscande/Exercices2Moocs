function ex_auv3d
%------------------------------------------------
    function draw(x)
        clf;axis([-25,25,-15,25,-10,25]);
        axis square;hold on;
        Auv0=[ 0  0  10  0   0   10   0   0 ;
            -1  1   0 -1  -0.2  0  0.2  1 ;
            0  0   0  0   1    0   1   0] ;
        Auv0=[Auv0;ones(1,length(Auv0))]; 
        E=eulermat(x(7),x(6),x(5)); %phi,theta,psi
        R=[E,[x(1);x(2);x(3)];0 0 0 1];
        Auv=R*Auv0; 
        plot3(Auv(1,:),Auv(2,:),Auv(3,:),'blue');
        plot3(Auv(1,:),Auv(2,:),0*Auv(3,:),'black'); % shadow
        drawnow();
    end
%------------------------------------------------------
    function xdot = f(x,u)
        v=x(4); psi=x(5); theta=x(6); phi=x(7);
        ct=cos(theta); st=sin(theta); tt=tan(theta);
        cf=cos(phi); sf=sin(phi); cp=cos(psi); sp=sin(psi);
        xdot=[v*ct*cp;v*ct*sp;-v*st;u(1);
            (sf/ct)*v*u(2)+(cf/ct)*v*u(3);
            cf*v*u(2)-sf*v*u(3);
            -0.1*sf*ct+tt*(sf*v*u(2)+cf*v*u(3))];
    end
%----------------  Main  ------------------------
init; dt=0.1;
x=[0;0;2;0.5;0;0;0];
for t=0:dt:10,
    u=[0;0;0];
    x=x+dt*f(x,u);
    draw(x);
end
end

