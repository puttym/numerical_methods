import numpy as np
from numpy import pi
from solver import solver, u_exact, solver_adjust_w

I = 1; w = 2*pi; dt = 0.1; num_periods = 8
P = 2*pi/w
T = P*num_periods

def test_three_steps():
    u_by_hand = np.array([1.000000000000000, 
                          0.802607911978128, 
                          0.28835892074005315])
    u, t = solver(I, w, dt, T)
    diff = np.abs(u_by_hand - u[:3]).max()
    tol = 1E-10
    assert diff < tol

def convergence_rates(m, solver_function, num_periods=8):
    dt = P/30

    dt_values = []
    E_values = []

    for i in range(m):
        u, t = solver_function(I, w, dt, T)
        u_e = u_exact(t, I, w)
        E = np.sqrt(dt*np.sum((u_e -u)**2))
        dt_values.append(dt)
        E_values.append(E)
        dt = dt/2

    r = [np.log(E_values[i-1]/E_values[i])/
        np.log(dt_values[i-1]/dt_values[i])
        for i in range(1, m, 1)]

    return r, E_values, dt_values

def test_convergence_rates():
    r, E, dt = convergence_rates(m=9, solver_function=solver, num_periods=8)
    tol = 0.1
    assert abs(r[-1] - 2.0) < tol 

    r, E, dt = convergence_rates(m=6, solver_function=solver_adjust_w, num_periods=8)
    print('Adjust w rates:', r)
    assert abs(r[-1] - 4.0) < tol