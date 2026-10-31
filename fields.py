import numpy as np

# Tokamak parameters (roughly SPARC-scale; adjust as you like)
R0 = 1.85    # major radius (m): distance from the machine's axis to the plasma center
B0 = 12.2    # toroidal field at R0 (T)
q = 2.0      # safety factor: how many times a field line goes around the long way per turn the short way

def B_field(pos):
    x, y, z = pos
    R = np.hypot(x, y)            # distance from the z-axis
    r = np.hypot(R - R0, z)       # distance from the plasma center circle (minor radius)

    #toroidal field B ~ 1/R
    B_phi = B0 * R0 / R 
    phi_hat = np.array([-y / R, x / R, 0.0])
    B = B_phi * phi_hat

    if r > 1e-12: #no poloidal field at the center of the plasma
        B_theta = (r / R) * B_phi / q
        theta_hat = np.array([-(z / r) * (x / R),
                              -(z / r) * (y / R),
                              (R - R0) / r])
        B = B + B_theta * theta_hat

    return B