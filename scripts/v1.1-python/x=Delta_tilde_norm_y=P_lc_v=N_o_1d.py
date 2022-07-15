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
# winding number
L_p         = 10
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

# frequently used variable
temp = 2 * g_tilde * N

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

# substituted variables
A_mathcal = temp * (omega_c_tilde - omega_d_tilde)
A_2 = A_mathcal**2 + Omega_c**2 * Omega_d**2
C = G**2 * (omega_c_tilde + omega_d_tilde) / np.sqrt(A_2)

# critical detuning 
Delta_tilde_cr = - np.sqrt(3) * gamma_o / 2
# frequency of the control laser
omega_lc = 2 * pi * c / lambda_lc
# critical power of the control laser
P_cr = gamma_o**2 * hbar * omega_lc / 3 / np.sqrt(3) / C / mu

# laser detuning normalized by critical values
Delta_tildes = np.linspace(-4, 4, 801) * gamma_o

# power of the control laser
P_lcs = np.array([0.25, 1.0, 2.25]) * P_cr

# detuning corresponding to multiple values of occupancy
Delta_tilde_norm_multis = list()
# multiple values of mean optical occupancy
N_o_multis = list()

################################################
##                  MAIN LOOP                 ##
################################################
# iterate control laser powers
for P_lc in P_lcs:
    # amplitude of the control laser
    eta_lc = np.sqrt(mu * gamma_o * P_lc / hbar / omega_lc)

    # temporary lists
    Delta_tilde_norm_multis_temp = list()
    N_o_multis_temp = list()

    # iterate control laser amplitudes
    for Delta_tilde in Delta_tildes:
        # coefficients of the cubic
        coeff_0 = 4 * C**2
        coeff_1 = 8 * C * Delta_tilde
        coeff_2 = 4 * Delta_tilde**2 + gamma_o**2
        coeff_3 = - 4 * np.real(np.conjugate(eta_lc) * eta_lc)
        # roots of the cubic
        roots = np.roots([coeff_0, coeff_1, coeff_2, coeff_3])
        # check each root
        for root in roots:
            # if root is real
            if np.imag(root) == 0.0:
                # update temporary lists
                Delta_tilde_norm_multis_temp.append(Delta_tilde / gamma_o)
                N_o_multis_temp.append(np.real(root))
    
    # update lists
    Delta_tilde_norm_multis.append(Delta_tilde_norm_multis_temp)
    N_o_multis.append(N_o_multis_temp)

################################################
##                    PLOTS                   ##
################################################
# colors
colors = ['b', 'g', 'r']
# linestyles
markers = ['o'] * 3
# plot
[plt.scatter(Delta_tilde_norm_multis[i], N_o_multis[i], c=colors[i], marker=markers[i], s=2) for i in range(len(P_lcs))]
# x-axis properties
plt.xlabel('$\\tilde{\\Delta} / \\gamma_{o}$')
plt.xlim(-4, 4)
# y-axis properties
plt.ylabel('$N_{o}$')
plt.ylim(0, 2e4)
# show
plt.show()
