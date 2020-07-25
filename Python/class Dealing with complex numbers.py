import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
        
    def __add__(self, no):
        return self.__str__(self.real+no.real,self.imaginary+no.imaginary)
        
    def __sub__(self, no):
        return self.__str__(self.real-no.real,self.imaginary-no.imaginary)
        
    def __mul__(self, no):
        return self.__str__((self.real*no.real)-(self.imaginary*no.imaginary),(self.real*no.imaginary)+(no.real*self.imaginary))
        
    def __truediv__(self, no):
        return self.__str__(((self.real*no.real)+(self.imaginary*no.imaginary))/(no.real**2+no.imaginary**2),(-(self.real*no.imaginary)+(self.imaginary*no.real))/(no.real**2+no.imaginary**2))
    
    def mod(self):
        return self.__str__(math.sqrt(self.real**2+self.imaginary**2),0)
    
    def __str__(self,a,b):
        if b == 0:
            result = "%.2f+0.00i" % (a)
        elif a == 0:
            if b >= 0:
                result = "0.00+%.2fi" % (b)
            else:
                result = "0.00-%.2fi" % (abs(b))
        elif b > 0:
            result = "%.2f+%.2fi" % (a,b)
        else:
            result = "%.2f-%.2fi" % (a, abs(b))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
