import numpy as np
import matplotlib.pyplot as plt

class MohrsCircle():
    def __init__(self,sigmax,sigmay,tauxy):
        ''' INPUT INITIAL INFORMATION
                σ_x : sigmax
                σ_y : sigmay
                τ_xy : tauxy  (shear stress on x-face)
        '''
        self.sigmax = sigmax
        self.sigmay = sigmay
        self.tauxy = tauxy

    def circleCenter(self):
        '''
        Calculate the value of center of the Mohrs circle which is the average of sigma x and sigma y
        '''
        return((self.sigmax + self.sigmay)/2)
    
    def radius(self):
        '''
        Calculate the radius of Mohrs circle which is the distance between center point and the point of tau_xy
        '''
        a = (self.sigmax-self.sigmay)/2
        b = self.tauxy
        return np.sqrt(a**2 + b**2)
    
    def maximumPrincipalStress(self):
        '''
        Return the value of center point of the circle added with the radius 
        '''
        return self.circleCenter() + self.radius()

    def minimumPrincipalStress(self):
        '''
        Return the value of center point of the circle subtracted with the radius 
        '''
        return self.circleCenter() - self.radius()

    def maximumShearStress(self):
        '''
        Return the value of radius of Mohrs circle
        '''        
        return self.radius()
    
    def mohrsCirclePlot(self):
        radians = np.linspace(0,360,361)*(2*np.pi/360)
        sigmapts = self.circleCenter() + self.radius()*np.cos(radians)
        taupts = self.radius()*np.sin(radians)

        # Figure size and lines
        plt.figure(figsize = [5,5])
        plt.fill_between(sigmapts,taupts,color='blue',alpha=0.1)
        plt.plot(sigmapts, taupts, label = "Mohrs' Circle", color = 'k')
        plt.plot([self.sigmax, self.sigmay],[self.tauxy, -self.tauxy], color = 'r')
        plt.plot([self.circleCenter()],[0], marker = 'o', color = 'k')

        # Stress labels on the graph
        plt.text(self.maximumPrincipalStress(), 0, r'$\sigma_{max}$', va = 'bottom', ha = 'right', fontsize = 14)
        plt.text(self.minimumPrincipalStress(), 0, r'$\sigma_{min}$', ha = 'left', va = 'bottom', fontsize = 14)
        plt.text(self.circleCenter(), self.maximumShearStress(), r'$\tau_{max}$', va='top', ha = 'center', fontsize = 14)  

        # Labels
        plt.title('Mohrs\' Circle',fontsize=18)
        plt.xlabel(r'$\sigma$',fontsize=14)
        plt.ylabel(r'$\tau$',fontsize=14)

        # Create horizontal and vertical lines at center
        plt.axhline(color = 'k')
        plt.axvline(color = 'k')

        #'Fits everything in one window'
        plt.tight_layout()
        plt.grid()
        plt.show()

if __name__ == '__main__':
    x1 = float(input('What is the value of sigmax ? '))
    x2 = float(input('What is the value of sigmay ? '))
    x3 = float(input('What is the value of tauxy ? '))

    y =MohrsCircle(x1,x2,x3)
    print('The maximum principal stress is ',round(y.maximumPrincipalStress(),2))
    print('The minimum principal stress is ',round(y.minimumPrincipalStress(),2))
    print('The maximum shear stress is ',round(y.maximumShearStress(),2))
    print('The center of the circle is ',round(y.circleCenter(),2))
    y.mohrsCirclePlot()


# Source : https://topdogengineer.com/object-oriented-programming-mohrs-circle/
#        : https://www.youtube.com/watch?v=lRUkVG25bUU 