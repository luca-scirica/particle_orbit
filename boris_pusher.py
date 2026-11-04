import numpy as np
import matplotlib.pyplot as plt
from fields import B_field, B0, R0

# proton
Q = 1.602176634e-19    # charge (C)
M = 1.67262192e-27     # mass (kg)

def boris_step(pos, v, dt, B_field_func=B_field):
    B = B_field_func(pos)
    t = (Q * B / M) * (dt / 2)
    s = 2 * t / (1 + np.dot(t, t))
    v_prime = v + np.cross(v, t)
    v_new = v + np.cross(v_prime, s)
    pos_new = pos + v_new * dt
    #print(np.linalg.norm(v_new)/np.linalg.norm(v)) # prints the ratio of the new velocity to the old velocity, which should be 1 for a purely magnetic field
    print(str(np.hypot(pos_new[0], pos_new[1])) + ", " + str(pos_new[2])) #prints R, z for each time step
    return pos_new, v_new

def simulate_trajectory(pos, v, dt, n_steps, B_field_func=B_field):
    steps_taken = 0
    while steps_taken < n_steps:
        pos, v = boris_step(pos, v, dt, B_field_func)
        steps_taken += 1
    return pos, v

def uniform_field(pos):
    return np.array([0.0, 0.0, B0])

#print(simulate_trajectory(np.array([R0, 0.0, 0.0]), np.array([0.0, 1e6, 0.0]), 1e-10, 400))
#simulate_trajectory(np.array([0, 0.0, 0.0]), np.array([1e6, 0.0, 0.0]), 1e-10, 400, uniform_field)