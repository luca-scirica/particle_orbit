import euler_pusher as ep
import boris_pusher as bp
import numpy as np
import matplotlib.pyplot as plt

def position_difference(pos, v, dt, n_steps):
    n = 0
    differences = []
    while n < n_steps:
        pos_euler, v_euler = ep.euler_step(pos, v, dt)
        pos_boris, v_boris = bp.boris_step(pos, v, dt)
        diff = pos_euler - pos_boris
        differences.append(np.linalg.norm(diff))
        #print(f"Step {n}: Position difference: {diff}, Norm: {np.linalg.norm(diff)}")
        pos = pos_euler  # Update position for the next step
        v = v_euler      # Update velocity for the next step
        n += 1
    return differences

def speed_difference(pos, v, dt, n_steps):
    n = 0
    differences = []
    while n < n_steps:
        pos_euler, v_euler = ep.euler_step(pos, v, dt)
        pos_boris, v_boris = bp.boris_step(pos, v, dt)
        speed_diff = np.linalg.norm(v_euler) - np.linalg.norm(v_boris)
        differences.append(speed_diff)
        #print(f"Step {n}: Speed difference: {speed_diff}")
        pos = pos_euler  # Update position for the next step
        v = v_euler      # Update velocity for the next step
        n += 1
    return differences



#plt.plot(np.arange(1,1001) * 1e-10, position_difference(np.array([ep.R0, 0.0, 0.0]), np.array([0.0, 1e6, 0.0]), 1e-10, 1000))#
#plt.xlabel("Time (s)")
#plt.ylabel("Position Difference (m)")
#plt.title("Comparison of Euler and Boris Pusher")
#plt.show()

plt.plot(np.arange(1,1001) * 1e-10, speed_difference(np.array([ep.R0, 0.0, 0.0]), np.array([0.0, 1e6, 0.0]), 1e-10, 1000))#
plt.xlabel("Time (s)")
plt.ylabel("Speed Difference (m/s)")
plt.title("Comparison of Euler and Boris Pusher")
plt.show()