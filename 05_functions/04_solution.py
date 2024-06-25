import math

def cicle(radius):

    area = math.pi * radius**2
    circumference =2* math.pi * radius
    rad = round(area,2)
    circumference=round(circumference,2)
    return rad,circumference
    
print(cicle(5))