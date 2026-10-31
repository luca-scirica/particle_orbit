import numpy as np
import matplotlib.pyplot as plt
from fields import B_field, B0, R0

# proton
Q = 1.602176634e-19    # charge (C)
M = 1.67262192e-27     # mass (kg)

def euler_step(pos, v, dt):
    B = B_field(pos)
    a = (Q / (M)) * np.cross(v, B)    # acceleration due to the magnetic field from the Lorentz force
    v_new = v + a * dt
    pos_new = pos + v_new * dt
    #print(np.linalg.norm(v_new)/np.linalg.norm(v)) # prints the ratio of the new velocity to the old velocity, which should be 1 for a purely magnetic field
    print(str(np.hypot(pos_new[0], pos_new[1])) + ", " + str(pos_new[2])) #prints R, z for each time step
    return pos_new, v_new

def simulate_trajectory(pos, v, dt, n_steps):
    steps_taken = 0
    while steps_taken < n_steps:
        pos, v = euler_step(pos, v, dt)
        steps_taken += 1
    return pos, v

print(simulate_trajectory(np.array([R0, 0.0, 0.0]), np.array([0.0, 1e6, 0.0]), 1e-10, 400))
