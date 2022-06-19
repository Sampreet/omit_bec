################################################
##               INITIALIZATION               ##
################################################
# matplotlib for plotting
import matplotlib.pyplot as plt
# numpy for numerics
import numpy as np
# scipy for constants
import scipy.constants as sc

# exact constants
amu = sc.physical_constants['atomic mass constant'][0]
c = sc.c
hbar = sc.hbar
pi = sc.pi

# # approximate constants used for PRL.127.113601
# amu = 1.6e-27
# c = 3e8
# hbar = 1.05e-34
# pi = 3.1416

# optomechanical coupling strength
G           = 2 * pi * 159
# normalized atom-atom interaction strength           
g_tilde_norm= 0.0
# mechanical damping rate
gamma_m     = 2 * pi * 0.8
# optical decay rate
gamma_o     = 2 * pi * 0.1e6
# OAM number
l           = 26
# frequency of control laser
lambda_lc   = 589e-9
# mass of Sodium atom
m           = 23
# laser-cavity coupling parameter
mu          = 0.5
# number of Sodium atoms
N           = 1e4
# radius of the ring-BEC
R           = 12e-6

# moment of inertia
I = m * amu * R**2

# atomic interactions
g_tilde = g_tilde_norm * hbar / 4 / I / N

# frequency of the control laser
omega_lc = 2 * pi * c / lambda_lc

# frequently used variable
temp = 2 * g_tilde * N

# detuning frequency with reference to a fixed offset
delta_offsets = np.linspace(-2, 2, 4001) * gamma_o

# winding numbers
L_ps = [50, 25, 0, -25, -50]

# probe detuning normalized by optical decay rate
delta_norms = list()
# transmission values
Ts = list()

################################################
##                  MAIN LOOP                 ##
################################################
# iterate winding numbers
for L_p in L_ps:
    # first sidemode
    omega_c = hbar * (L_p + 2 * l)**2 / 2 / I
    omega_c_tilde = omega_c + temp
    Omega_c = np.sqrt((omega_c + 2 * temp)**2 - temp**2)
    # second sidemode
    omega_d = hbar * (L_p - 2 * l)**2 / 2 / I
    omega_d_tilde = omega_d + temp
    Omega_d = np.sqrt((omega_d + 2 * temp)**2 - temp**2)
    # sum and differences
    Omega_m = (Omega_c + Omega_d) / 2
    Omega_n = (Omega_c - Omega_d)
    
    # create lists for comprehension
    omega_tildes = [omega_c_tilde, omega_d_tilde]
    Omegas = [Omega_c, Omega_d]

    # substituted variables
    A_mathcal = temp * (omega_c_tilde - omega_d_tilde)
    A_2 = A_mathcal**2 + Omega_c**2 * Omega_d**2
    C = G**2 * (omega_c_tilde + omega_d_tilde) / np.sqrt(A_2)

    # critical power of control laser
    P_cr = gamma_o**2 * hbar * omega_lc / 3 / np.sqrt(3) / C / mu

    ############################################
    # power of the control laser
    P_lc = 0.002**2 * P_cr
    # amplitude of the control laser
    eta_lc = np.sqrt(mu * gamma_o * P_lc / hbar / omega_lc)
    # detuning of the control laser
    Delta_tilde = - Omega_n
    ############################################
        
    # effective detuning
    Delta = Delta_tilde
    # mean optical amplitude
    alpha_s = eta_lc / (gamma_o / 2 - 1j * Delta)
    # mean optical occupancy
    N_o = np.real(np.conjugate(alpha_s) * alpha_s)

    # temporary lists
    delta_norms_temp = list()
    Ts_temp = list()

    # iterate offset probe detunings
    for delta_offset in delta_offsets:
        ########################################
        # offset for probe detuning
        offset = Omega_n
        # probe detuning
        delta = delta_offset + offset
        ########################################

        # effective decay rates
        Gamma_m = gamma_o / 2 - 1j * (Delta + delta)
        Gamma_p = gamma_o / 2 + 1j * (Delta - delta)

        # effective susceptibilities
        chis =  [1 / (Omegas[i]**2 - 1j * delta * gamma_m - delta**2) for i in range(2)]

        # numerator of Lambda
        _num = A_mathcal * chis[0] * chis[1] * (omega_c - omega_d)
        _num += sum([chis[i] * omega_tildes[i] for i in range(2)])
        # denominator of Lambda
        _den = A_mathcal**2 * chis[0] * chis[1] + 1
        # Lambda
        Lambda = _num / _den

        # transmission coefficeint without any approximation
        _num_s = mu * gamma_o * (Gamma_p + 1j * G**2 * Lambda * N_o)
        _den = Gamma_m * Gamma_p + 2 * Delta * G**2 * Lambda * N_o
        t_s = 1 - _num_s / _den

        # transmission
        T = np.real(np.conjugate(t_s) * (t_s))

        # update temporary lists
        delta_norms_temp.append(delta / gamma_o)
        Ts_temp.append(T)
    
    # update lists
    delta_norms.append(delta_norms_temp)
    Ts.append(Ts_temp)

################################################
##                    PLOTS                   ##
################################################
# colors
colors = ['b', 'g', 'k', 'g', 'b']
# linestyles
linestyles = ['-', '-', '-', '--', '--']
# plot
[plt.plot(delta_norms[i], Ts[i], colors[i], linestyle=linestyles[i]) for i in range(len(Ts))]
# x-axis properties
plt.xlabel('$\delta / \gamma_{o}$')
plt.xlim(-1, 1)
# y-axis properties
plt.ylabel('$T$')
plt.ylim(0, 1)
# show
plt.show()
