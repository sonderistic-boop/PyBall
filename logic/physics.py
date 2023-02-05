import pygame as pg


#given two objects, objects, with mass, velocity and restitution, 
#simulate a physics collision between them, and 
#return the new velocities of the objects after the collision
def collision_ball(obj1,obj2):


    normalVector = ((obj2.position + pg.math.Vector2(obj2.w//2,obj2.h//2)) - (obj1.position + pg.math.Vector2(obj1.w//2,obj1.h//2))).normalize()
    
    relativeVelocity = obj2.velocity - obj1.velocity

    normalVelocity = relativeVelocity.dot(normalVector)

    if(normalVelocity > 0):
        return
    
    e = min(obj1.restitution,obj2.restitution)

    j = -(1+e) * normalVelocity / (obj1.inverseMass + obj2.inverseMass)

    impulse = normalVector * j

    obj1.velocity -= impulse * (obj1.inverseMass)
    obj2.velocity += impulse * (obj2.inverseMass)
    #floating_error(obj1,obj2,normal_vector)



#obj1 gets kicked by obj2
def thrust(obj1,obj2):
    e = min(obj1.restitution,obj2.restitution)
    normalVector = ((obj2.position + pg.math.Vector2(obj2.w//2,obj2.h//2)) - (obj1.position + pg.math.Vector2(obj1.w//2,obj1.h//2))).normalize()
    obj1.velocity = normalVector * 6 *-(1+e)







"""
def floating_error(obj1,obj2,normalVector):

    magnitude = normalVector.magnitude()
    penetrationDepth = -(magnitude - obj1.radius - obj2.radius)
    
    slack = 0.6

    allowance = 0.001
  
    correction = max(penetrationDepth - slack, 0 ) / (obj1.inverseMass + obj2.inverseMass) * allowance * normalVector
    obj1.position -= obj1.inverseMass * correction
    obj2.position += obj2.inverseMass * correction

"""
