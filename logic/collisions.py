#given two objects, objects, with mass, velocity and restitution, 
#simulate a physics collision between them, and 
#return the new velocities of the objects after the collision
def collision_ball(obj1,obj2):
    relative_velocity = (obj1.velocity - obj2.velocity)
    e = min(obj1.restitution,obj2.restitution)