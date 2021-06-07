import numpy as np
import matplotlib.pyplot as plt

# input
u = 40 # initial velocity in m/s
g = 9.81 # gravitational acceleration m/s^2

theta1 = 45 # angle of projectile
theta2 = 60 # angle of projectile

ux1 = u*np.cos(theta1*np.pi/180) # velocity in x direction
uy1 = u*np.sin(theta1*np.pi/180) # velocity in y direction

ux2  = u*np.cos(theta2*np.pi/180) # velocity in x direction
uy2 = u*np.sin(theta2*np.pi/180) # velocity in y direction

t_total_1 = 2*uy1/g
t_total_2 = 2*uy2/g


t1 = np.linspace(0,t_total_1,100)
t2 = np.linspace(0,t_total_2,100)

x1 = ux1*t1
y1 = (uy1*t1)-(0.5*g*t1**2)

x2 = ux2*t2
y2= (uy2*t2)-(0.5*g*t2**2)

plt.figure(figsize=(10,7)) # set graph size
plt.margins(x=0) # set x axis margin
plt.title('Projectile motion')
plt.plot(x1,y1,label = r'$\theta$ = 45$\degree$')
plt.plot(x2,y2,label = r'$\theta$ = 60$\degree$',color='red')
plt.legend()
plt.show()

# https://www.udemy.com/user/shriram-s-kakade/