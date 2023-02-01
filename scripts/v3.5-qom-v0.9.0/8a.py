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
            'var': 'delta',
            'min': -0.5,
            'max': 0.5,
            'dim': 10001
        },
        'Y': {
            'var': 'Delta_tilde',
            'val': [-0.8, -0.9, -1.0, -1.1, -1.2]
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
        'L_p'           : 1,
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
        't_oss_method'  : 'basic',
        't_P_lc_norm'   : 'none'
    },
    'plotter': {
        'type': 'lines_3d',
        'x_label_pad': 32,
        'x_label': '$\\left( \\delta - \\Omega_{m} \\right) / \\Omega_{m}$',
        'x_tick_pad': 0,
        'x_ticks': [-0.5, 0.0, 0.5],
        'x_ticks_minor': [i * 0.25 - 0.5 for i in range(5)],
        'y_label_pad': 48,
        'y_label': '$\\tilde{\\Delta} / \\Omega_{m}$',
        'y_limits': [-1.22, -0.78],
        'y_tick_labels': [-1.2, -1.1, -1.0, -0.9, -0.8],
        'y_tick_pad': 4,
        'y_ticks': [i * 0.1 - 1.2 for i in range(5)],
        'y_ticks_minor': [i * 0.1 - 1.2 for i in range(5)],
        'y_colors': ['k', 'r', 'g', 'b', 'm'],
        'y_sizes': [2] * 5,
        'v_label_pad': 20,
        'v_label': '$T$',
        'v_tick_pad': 8,
        'v_ticks': [0.0, 0.5, 1.0],
        'v_ticks_minor': [i * 0.1 for i in range(11)],
        'view_aspect': [1.0, 1.5, 0.75],
        'view_elevation': 28,
        'view_rotation': -45,
        'annotations': [{
            's': '(a)',
            'xy': (0.14, 0.66)
        }],
        'label_font_size': 32.0,
        'tick_font_size': 26.0,
        'height': 8.0,
        'width': 9.6
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_10, params=params, func='transmission', looper='XYLooper', plot=True)