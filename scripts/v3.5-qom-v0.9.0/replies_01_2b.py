# dependencies
import numpy as np
import os 
import sys

# qom modules
from qom.ui.plotters import MPLPlotter
from qom.utils.looper import wrap_looper

# add path to local libraries
sys.path.append(os.path.abspath(os.path.join('..', 'bec-systems')))
# import system
from systems import BEC_10

# all parameters
params = {
    'looper': {
        'X': {
            'var': 'P_lc',
            'min': 0.0e-15,
            'max': 1.5e-15,
            'dim': 151
        }
    },
    'system': {
        'Delta_tilde'   : -1.0,
        'delta'         : 0.0,
        'G'             : 2 * np.pi * 1e3,
        'g_tilde_norm'  : 0.0,
        'gamma_m'       : 2 * np.pi * 0.8,
        'gamma_o'       : 2 * np.pi * 1e3,
        'k'             : 1,
        'L_p'           : 0,
        'l'             : 20,
        'lambda_lc'     : 589e-9,
        'm'             : 23,
        'mu'            : 0.5,
        'N'             : 1e4,
        'P_lc'          : 1e-15,
        'P_lp_norm'     : 0.01,
        'R'             : 10e-6,
        't_approx'      : 'res',
        't_Delta_norm'  : 'Omega_m',
        't_Delta_offset': 'zero',
        't_delta_norm'  : 'Omega_m',
        't_delta_offset': 'Omega_m',
        't_line'        : 's',
        't_oss_method'  : 'basic',
        't_P_lc_norm'   : 'none'
    },
    'plotter': {
        'type': 'lines',
        'x_label': '$P_{lc}$ (fW)',
        'x_tick_labels': [0.0, 0.5, 1.0, 1.5],
        'x_ticks': [0.0e-15, 0.5e-15, 1.0e-15, 1.5e-15],
        'x_ticks_minor': [i * 0.1e-15 for i in range(16)],
        'y_colors': ['b', 'r'],
        'y_sizes': [2] * 2,
        'y_styles': ['-'] * 2,
        'v_label': '$\\mathcal{C}$',
        'v_label_color': 'b',
        'v_ticks': [i * 50 for i in range(6)],
        'v_ticks_minor': [i * 25 for i in range(11)],
        'v_twin_label': '$\\frac{N}{10^{8}} \\times \\left( \\frac{g_{a}^{2}}{2 \sqrt{2} \\Delta_{a}} \\right)^{2}$',
        'v_twin_label_color': 'r',
        'v_twin_tick_labels': [i for i in range(6)],
        'v_twin_ticks': [i * 1e8 for i in range(6)],
        'v_twin_ticks_minor': [i * 0.5e8 for i in range(11)],
        'label_font_size': 32.0,
        'tick_font_size': 26.0,
        'height': 8.0,
        'width': 9.6
    }
}

# function to calculate average measure in decibels
def func_transmission_N_os(system_params, val, logger, results):
    # initialize system
    system = BEC_10(params=system_params)
    # extract parameters
    iv, c = system.get_ivc()
    _, params = system._get_D_params_ivp(c)
    # get transparency
    value = system.get_transmission(params=params)
    # get mean optical occupancies
    N_os = system.get_N_os(params=params)
    # update results
    results.append((val, [value, N_os]))

# looper
looper = wrap_looper(SystemClass=BEC_10, params=params, func=func_transmission_N_os, looper='XLooper', plot=False)
xs = looper.axes['X']['val']
vs = looper.results['V']
Ts = [v[0] for v in vs]
C_mathcals = [np.sqrt(t) / (1 - np.sqrt(t)) for t in Ts]
N_os = [v[1][0] for v in vs]
gamma_m = params['system']['gamma_m']
gamma_o = params['system']['gamma_o']
N_norm = [C_mathcals[i] * gamma_m * gamma_o / N_os[i] for i in range(len(C_mathcals))]

# plotter
plotter = MPLPlotter(axes={
    'X': xs
}, params=params['plotter'])
plotter.update(xs=xs, vs=C_mathcals)
plotter.update_twin_axis(xs=xs, vs=N_norm)
plotter.show(True)