from matplotlib_settings import set_plot_defaults
import matplotlib.pyplot as plt
from solver import u_exact, solver, solver_adjust_w
from test import convergence_rates
import numpy as np
from plotslopes import slope_marker

set_plot_defaults()

def visualise(u, t, dt, I, w):
    fig = plt.figure(figsize=(12, 8)) #Create an instance of the class figure
    ax = fig.subplots(nrows=1, ncols=1) #Create an instance of the class AxesSubplot
    t_fine = np.linspace(0, t[-1], 1001)
    u_e = u_exact(t_fine, I, w)
    ax.plot(t, u, 'r--o', label='numerical')
    ax.plot(t_fine, u_e, 'b-', label='exact')
    ax.set(title='dt = %g' % dt, xlabel='t', ylabel='u')
    umin = 1.2*u.min(); umax = -umin
    ax.axis([t[0]-(0.05*t[-1]), t[-1]+(0.05*t[-1]), umin, umax])
    ax.legend(loc='upper right', ncol=2, fontsize=8, frameon=False)
    plt.show()
    fig.savefig('t2.png')

def plot_convergence_rates():
    r2, E2, dt2 = convergence_rates(m=5, solver_function=solver, num_periods=8)
    plt.loglog(dt2, E2)

    r4, E4, dt4 = convergence_rates(m=5, solver_function=solver_adjust_w, num_periods=8)
    plt.loglog(dt4, E4)
    plt.legend(['original scheme', r'adjusted $\omega$'], loc='upper left')
    plt.title('Convergence of FD methods')
    plt.xlabel(r'$\ln\, \Delta t$')
    plt.ylabel(r'$\ln\, E$')

    slope_marker((dt2[1], E2[1]), (2,1))
    slope_marker((dt4[1], E4[1]), (4,1))
    plt.savefig('convergence.png')
    plt.show()
    plt.close()

if __name__ == "__main__":
    plot_convergence_rates()