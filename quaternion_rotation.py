import numpy as np

angle = actual_angle/2 

point = [x, y, z] #point to rotate

normal_vector = [x, y, z] # vector to rotate around

def turn_4D(point, normal_vector):
	v = [0, point[0], point[1], point[2]]
	
	np.linalg.norm(normal_vector)
	q = [np.cos(angle), normal_vector[0]*np.sin(angle),
	normal_vector[1]*np.sin(angle), normal_vector[2]*np.sin(angle)]
	return v, q

def conjugate(q):
	w,x,y,z = q
	return [w, -x, -y, -z]

def quaternion_mult(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    return [w,x,y,z]

def quaternion_rotation(punt, q):
	sub_product = quaternion_mult(q,v)
	return quaternion_mult(sub_product, conjugate(q))

v, q = turn_4D(point, normal_vector)
v_prime = quaternion_rotation(v, q) 