import numpy as np

def solver(I, w, dt, T):
    Nt = T/dt
    Nt = round(Nt) # We requite Nt to be an integer. round() returns an integer
    T = Nt * dt # Resetting T according to the integer value of Nt
    t = np.linspace(0, T, Nt+1) # Mesh
    u = np.zeros(len(t)) # Arry to store the mesh function

    u[0] = I # Initial condition
    u[1] = u[0] - (0.5 * dt**2 * w**2 * u[0])

    for n in range(1, Nt): # Runs from 1 to Nt-1 
        u[n+1] = 2*u[n] - u[n-1] - w**2*u[n]*dt**2 # Computes from u[2] to u[Nt]. Nt-1 values
    return u, t

def solver_adjust_w(I, w, dt, T, adjust_w=True):
    Nt = T/dt
    Nt = round(Nt)
    T = Nt * dt
    t = np.linspace(0, T, Nt+1)
    u = np.zeros(len(t))
    w_adj = w*(1 - w**2*dt**2/24) if adjust_w else w

    u[0] = I # Initial condition
    u[1] = u[0] - (0.5 * dt**2 * w_adj**2 * u[0])

    for n in range(1, Nt): # Runs from 1 to Nt-1 
        u[n+1] = 2*u[n] - u[n-1] - w_adj**2*u[n]*dt**2 # Computes from u[2] to u[Nt]. Nt-1 values
    return u, t

def u_exact(t, I, w):
    return I*np.cos(w*t)

if __name__ == "__main__":
    solver(I, w, dt, T)