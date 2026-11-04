A small Python project that follows a single charged particle (a proton) through a simplified tokamak magnetic field. The goal is to understand how particle orbits behave in magnetic confinement and to build and validate the numerical tools needed to study them.

Status: work in progress. So far the project covers the field model, two integrators (Boris and forward Euler), and validation of the Boris pusher against an analytic solution in a uniform field. Tests in the full tokamak field are still to do.

Contents:

fields.py	        Simplified tokamak magnetic field B_field(pos)
pusher.py	        Boris integrator and a single-orbit test
euler_pusher.py	    Forward-Euler integrator, written as a comparison case
boris_pusher.py     Boris pusher
analytic test.py	Comparison against the analytic solution and the convergence test
visualize.py        Visualizes particle trajectories
compare.py          Compares Euler and Boris models and shows divergence


Model:

Geometry - the torus axis is the z-axis. Major radius R0 = 1.85 m, toroidal field B0 = 12.2 T at R0 (roughly SPARC-scale numbers), safety factor q = 2.
Toroidal field - B_phi = B0 * R0 / R, falling off as 1/R.
Poloidal field - large-aspect-ratio approximation with constant q, which twists the field lines into helices.
Particle - a proton moving non-relativistically under the Lorentz force. There is no electric field.

Methods:

Boris pusher. Rotates particle velocity around magnetic field according to omega and dt, and moves the particle according to this, preserving speed.

Forward Euler. Included deliberately as a naive baseline: v += (Q/M) (v x B) dt, then x += v dt.

Results:

1. Forward Euler gains energy

The magnetic force is always perpendicular to the velocity, but Euler slightly lengthens the perpendicular velocity. The speed is multiplied by about sqrt(1 + (omega*dt)^2) per step.

2. Boris matches the analytic orbit in a uniform field

For a proton starting at the origin with velocity (v, 0, 0) in a uniform field (0, 0, B), the exact orbit is a circle:

x(t) =  (v/omega) sin(omega t)
y(t) = -(v/omega) (1 - cos(omega t))

Boris reproduces it, including the rotation direction. There is a slow phase drift: Boris rotates by 2 arctan(omega*dt/2) per step instead of omega*dt. Before adding the half-step velocity stagger, there was also a constant offset from the start-up error, which disappeared once the stagger was added.

3. Convergence: second order

At a fixed total time T, I ran Boris at several time steps from 1e-10 s to 1e-12 s and recorded the maximum position error against the analytic solution. On log-log axes the error follows a straight line with slope 2, consistent with second-order accuracy: halving dt reduces the error by about 4x.
