import math

class cone():    
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
            
    def volume(self):
         return self.height * math.pi * (self.radius**2) * 1/3

    def surface_area(self):
        return  math.pi * self.radius**2 + math.pi * self.radius * math.sqrt(self.height**2 + self.radius**2)


    
p=cone(12,14)
print( "{:.2f}".format( p.volume() ) )
print( "{:.2f}".format( p.surface_area() ) ) 
