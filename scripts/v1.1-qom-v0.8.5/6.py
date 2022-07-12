# dependencies
import numpy as np
import os 
import sys

# qom modules
from qom.utils.looper import wrap_looper

# add path to local libraries
sys.path.append(os.path.abspath(os.path.join('..', 'bec-systems')))
# import system
from systems import BEC_10

# frequently used variables
gamma_o = 2 * np.pi * 0.1e6

# all parameters
params = {
    'looper': {
        'X': {
            'var': 'delta_offset',
            'min': -4 * gamma_o ,
            'max': 4 * gamma_o,
            'dim': 1001
        },
        'Y': {
            'var': 'L_p',
            'val': [50, 25, 0, -25, -50]
        }
    },
    'system': {
        'Delta_tilde': 0.0,
        'delta_offset': 0.0,
        'G': 2 * np.pi * 159,
        'g_tilde_norm': 0.0,
        'gamma_m': 2 * np.pi * 0.8,
        'gamma_o': gamma_o,
        'k': 1,
        'L_p': 10,
        'l': 26,
        'lambda_lc': 589e-9,
        'm': 23,
        'mu': 0.5,
        'N': 1e4,
        'P_lc': 4e-6,
        'P_lp_norm': 0.01,
        'R': 12e-6,
        't_approx': 'none',
        't_detuning': '-Omega_n',
        't_line': 's',
        't_offset': 'none',
        't_oss_method': 'basic',
        't_P_lc': 'norm'
    },
    'plotter': {
        'type': 'lines',
        'x_label': '$\\delta / \gamma_{o}$',
        'x_tick_labels': [i - 2 for i in range(5)],
        'x_ticks': [(i - 2) * gamma_o for i in range(5)],
        'x_ticks_minor': [(i - 8) * 0.25 * gamma_o for i in range(17)],
        'y_colors': ['b', 'r', 'k', 'r', 'b'],
        'y_name': '$L_{p}$',
        'y_sizes': [1] * 5,
        'y_styles': ['-'] * 3 + ['--'] * 2,
        'v_label': '$T$',
        'v_tick_labels': ['{:1.1f}'.format(i * 0.5) for i in range(3)],
        'v_ticks': [i * 0.5 for i in range(3)],
        'v_ticks_minor': [i * 0.1 for i in range(11)],
        'show_legend': True,
        'legend_location': 'lower left',
        'legend_font_size': 12.0,
        'height': 3.6,
        'width': 4.8
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_10, params=params, func='transmission', looper='XYLooper', plot=True)