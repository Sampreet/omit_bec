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

# all parameters
params = {
    'looper': {
        'X': {
            'var': 'P_lc',
            'min': 0.0,
            'max': 90e-15,
            'dim': 9001,
            'scale': 'linear'
        },
        'Y': {
            'var': 'g_tilde_norm',
            'val': [0.0, 12.0]
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
        't_approx'      : 'none',
        't_Delta_norm'  : 'Omega_m',
        't_Delta_offset': 'zero',
        't_delta_norm'  : 'Omega_m',
        't_delta_offset': 'Omega_m',
        't_line'        : 's',
        't_oss_method'  : 'cubic',
        't_P_lc_norm'   : 'none'
    },
    'plotter': {
        'type': 'scatters',
        'x_label': '$P_{lc}$ (fW)',
        'x_tick_labels': [i * 15 for i in range(7)],
        'x_tick_pad': 16,
        'x_ticks': [i * 15e-15 for i in range(7)],
        'x_ticks_minor': [i * 5e-15 for i in range(19)],
        'y_colors': ['b', 'k'],
        'y_legend': ['$\\tilde{g} = 0$', '$\\tilde{g} = 12 \\tilde{g}_{m}$', '$\\tilde{g} = 40 \\tilde{g}_{m}$'],
        'y_sizes': [10, 10],
        'y_styles': ['s', '.'],
        'v_label': '$\\left| \\alpha_{s} \\right|^{2}$',
        'v_tick_pad': 16,
        'v_ticks': [i * 2 for i in range(6)],
        'v_ticks_minor': [i * 0.5 for i in range(21)],
        'show_legend': True,
        'legend_location': 'center right',
        'annotations': [{
            's': '(a)',
            'xy': (0.19, 0.86)
        }],
        'legend_font_size': 32.0,
        'label_font_size': 40.0,
        'tick_font_size': 32.0,
        'height': 8.0,
        'width': 9.6
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_10, params=params, func='N_os', looper='XYLooper', plot=True)