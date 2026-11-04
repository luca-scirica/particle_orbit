import euler_pusher as ep
import boris_pusher as bp
import numpy as np
import matplotlib.pyplot as plt
import fields as fld

def simple_cyclotron(t):

    Q = 1.602176634e-19  # Charge of the proton (C)
    M = 1.67262192e-27   # Mass of the proton (kg)
    B = fld.B0  # Magnetic field strength (T)

    omega_c = Q * B / M

    # Position in the x-y plane
    x = 1e6 / omega_c * np.sin(omega_c * t)
    y = - 1e6 / omega_c * ( 1 - np.cos(omega_c * t))

    return x, y

def graph_solutions(pos, v, dt, n_steps, B_field_func=fld.B_field, analytical_solution_func=None):
    steps_taken = 0
    x_positions = []
    y_positions = []
    times = []
    v = bp.boris_step(pos, v, -dt / 2, B_field_func)[1]  # Half-step back in velocity
    while steps_taken < n_steps:
        pos, v = bp.boris_step(pos, v, dt, B_field_func)
        steps_taken += 1
        x_positions.append(pos[0])
        y_positions.append(pos[1])
        times.append(steps_taken * dt)
    x_analytical_solution = []
    y_analytical_solution = []
    for time in times:
        x_analytical, y_analytical = analytical_solution_func(time)
        x_analytical_solution.append(x_analytical)
        y_analytical_solution.append(y_analytical)
    fig, (xs, ys, diffs) = plt.subplots(3)
    xs.plot(times, x_analytical_solution, label="Analytical")
    xs.plot(times, x_positions, label="Boris")
    xs.set_xlabel("Time (s)")
    xs.set_ylabel("X Position (m)")
    xs.set_title("X Position vs Time")
    ys.plot(times, y_analytical_solution, label="Analytical")
    ys.plot(times, y_positions, label="Boris")
    ys.set_xlabel("Time (s)")
    ys.set_ylabel("Y Position (m)")
    ys.set_title("Y Position vs Time")
    diffs.plot(times, np.array(x_positions) - np.array(x_analytical_solution), label="X Difference")
    diffs.plot(times, np.array(y_positions) - np.array(y_analytical_solution), label="Y Difference")
    diffs.set_xlabel("Time (s)")
    diffs.set_ylabel("Position Difference (m)")
    plt.show()
    return

def graph_euler_solutions(pos, v, dt, n_steps, B_field_func=fld.B_field, analytical_solution_func=None):
    steps_taken = 0
    x_positions = []
    y_positions = []
    times = []
    while steps_taken < n_steps:
        pos, v = ep.euler_step(pos, v, dt, B_field_func)
        steps_taken += 1
        x_positions.append(pos[0])
        y_positions.append(pos[1])
        times.append(steps_taken * dt)
    x_analytical_solution = []
    y_analytical_solution = []
    for time in times:
        x_analytical, y_analytical = analytical_solution_func(time)
        x_analytical_solution.append(x_analytical)
        y_analytical_solution.append(y_analytical)
    fig, (xs, ys, diffs) = plt.subplots(3)
    xs.plot(times, x_analytical_solution, label="Analytical")
    xs.plot(times, x_positions, label="Boris")
    xs.set_xlabel("Time (s)")
    xs.set_ylabel("X Position (m)")
    xs.set_title("X Position vs Time")
    ys.plot(times, y_analytical_solution, label="Analytical")
    ys.plot(times, y_positions, label="Boris")
    ys.set_xlabel("Time (s)")
    ys.set_ylabel("Y Position (m)")
    ys.set_title("Y Position vs Time")
    diffs.plot(times, np.array(x_positions) - np.array(x_analytical_solution), label="X Difference")
    diffs.plot(times, np.array(y_positions) - np.array(y_analytical_solution), label="Y Difference")
    diffs.set_xlabel("Time (s)")
    diffs.set_ylabel("Position Difference (m)")
    plt.show()
    return

graph_solutions(np.array([0, 0.0, 0.0]), np.array([1e6, 0.0, 0.0]), 1e-10, 30, fld.uniform_field, simple_cyclotron)