import pygame as pg


#given two objects, objects, with mass, velocity and restitution, 
#simulate a physics collision between them, and 
#return the new velocities of the objects after the collision
def collision_ball(obj1,obj2):


    normal_vector = ((obj2.position + pg.math.Vector2(obj2.w//2,obj2.h//2)) - (obj1.position + pg.math.Vector2(obj1.w//2,obj1.h//2))).normalize()
    
    relative_velocity = obj2.velocity - obj1.velocity

    normal_velocity = relative_velocity.dot(normal_vector)

    if(normal_velocity > 0):
        return
    
    e = min(obj1.restitution,obj2.restitution)

    j = -(1+e) * normal_velocity / (obj1.inverse_mass + obj2.inverse_mass)

    impulse = normal_vector * j

    obj1.velocity -= impulse * (obj1.inverse_mass)
    obj2.velocity += impulse * (obj2.inverse_mass)
    #floating_error(obj1,obj2,normal_vector)



#obj1 gets kicked by obj2
def kick_ball(obj1,obj2):
    e = min(obj1.restitution,obj2.restitution)
    normal_vector = ((obj2.position + pg.math.Vector2(obj2.w//2,obj2.h//2)) - (obj1.position + pg.math.Vector2(obj1.w//2,obj1.h//2))).normalize()
    obj1.velocity = normal_vector * 6 *-(1+e)








def floating_error(obj1,obj2,normal_vector):

    magnitude = normal_vector.magnitude()
    penetration_depth = -(magnitude - obj1.radius - obj2.radius)
    
    slack = 0.6

    allowance = 0.001
  
    correction = max(penetration_depth - slack, 0 ) / (obj1.inverse_mass + obj2.inverse_mass) * allowance * normal_vector
    obj1.position -= obj1.inverse_mass * correction
    obj2.position += obj2.inverse_mass * correction

