import euler_pusher as ep
import boris_pusher as bp
import numpy as np
import matplotlib.pyplot as plt

def z_trajectory(pos, v, dt, n_steps):
    steps_taken = 0
    z_positions = []
    time = []
    while steps_taken < n_steps:
        pos, v = bp.boris_step(pos, v, dt)
        steps_taken += 1
        z_positions.append(pos[2])
        time.append(steps_taken * dt)
    plt.plot(time, z_positions)
    plt.xlabel("Time (s)")
    plt.ylabel("Z Position (m)")
    plt.title("Z Position vs Time")
    plt.show()
    return

def R_trajectory(pos, v, dt, n_steps):
    steps_taken = 0
    R_positions = []
    time = []
    while steps_taken < n_steps:
        pos, v = bp.boris_step(pos, v, dt)
        steps_taken += 1
        R_positions.append(np.linalg.norm([pos[0], pos[1]]))
        time.append(steps_taken * dt)
    plt.plot(time, R_positions)
    plt.xlabel("Time (s)")
    plt.ylabel("Radial Position (m)")
    plt.title("Radial Position vs Time")
    plt.show()
    return

R_trajectory(np.array([ep.R0, 0.0, 0.0]), np.array([0.0, 1e6, 0.0]), 5e-9, 400)