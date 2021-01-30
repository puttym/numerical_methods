from solver import solver
from visualise import visualise, plot_convergence_rates
from command_line_args import command_line_args

import numpy as np
from matplotlib_settings import set_plot_defaults
import matplotlib.pyplot as plt
from numpy import pi

def main():
    I, w, dt, num_periods = command_line_args()
    P = 2*pi/w
    T = P*num_periods
    u, t = solver(I, w, dt, T)
    visualise(u, t, dt, I, w)
    plot_convergence_rates()


if __name__ == "__main__":
    main()