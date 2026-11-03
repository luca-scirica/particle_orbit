import euler_pusher as ep
import boris_pusher as bp
import numpy as np
import matplotlib.pyplot as plt
import fields as fld

def z_trajectory(pos, v, dt, n_steps, B_field_func=fld.B_field):
    steps_taken = 0
    z_positions = []
    time = []
    while steps_taken < n_steps:
        pos, v = bp.boris_step(pos, v, dt, B_field_func)
        steps_taken += 1
        z_positions.append(pos[2])
        time.append(steps_taken * dt)
    plt.plot(time, z_positions)
    plt.xlabel("Time (s)")
    plt.ylabel("Z Position (m)")
    plt.title("Z Position vs Time")
    plt.show()
    return

def x_trajectory(pos, v, dt, n_steps, B_field_func=fld.B_field):
    steps_taken = 0
    x_positions = []
    time = []
    while steps_taken < n_steps:
        pos, v = bp.boris_step(pos, v, dt, B_field_func)
        steps_taken += 1
        x_positions.append(pos[0])
        time.append(steps_taken * dt)
    plt.plot(time, x_positions)
    plt.xlabel("Time (s)")
    plt.ylabel("X Position (m)")
    plt.title("X Position vs Time")
    plt.show()
    return

def y_trajectory(pos, v, dt, n_steps, B_field_func=fld.B_field):
    steps_taken = 0
    y_positions = []
    time = []
    while steps_taken < n_steps:
        pos, v = bp.boris_step(pos, v, dt, B_field_func)
        steps_taken += 1
        y_positions.append(pos[1])
        time.append(steps_taken * dt)
    plt.plot(time, y_positions)
    plt.xlabel("Time (s)")
    plt.ylabel("Y Position (m)")
    plt.title("Y Position vs Time")
    plt.show()
    return


def R_trajectory(pos, v, dt, n_steps, B_field_func=fld.B_field):
    steps_taken = 0
    R_positions = []
    time = []
    while steps_taken < n_steps:
        pos, v = bp.boris_step(pos, v, dt, B_field_func)
        steps_taken += 1
        R_positions.append(np.linalg.norm([pos[0], pos[1]]))
        time.append(steps_taken * dt)
    plt.plot(time, R_positions)
    plt.xlabel("Time (s)")
    plt.ylabel("Radial Position (m)")
    plt.title("Radial Position vs Time")
    plt.show()
    return

x_trajectory(np.array([0.0, 0.0, 0.0]), np.array([0.0, 1e6, 0.0]), 1e-10, 400, fld.uniform_field)
y_trajectory(np.array([0.0, 0.0, 0.0]), np.array([0.0, 1e6, 0.0]), 1e-10, 400, fld.uniform_field)

