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
gamma_o = 2 * np.pi * 1e3

# all parameters
params = {
    'looper': {
        'X': {
            'var': 'delta_offset',
            'min': 2.0 * gamma_o,
            'max': 6.0 * gamma_o,
            'dim': 40001
        },
        'Y': {
            'var': 'L_p',
            'val': [10, 5, 0, -5, -10]
        }
    },
    'system': {
        'Delta_tilde': 0.0,
        'delta_offset': 0.0,
        'G': 2 * np.pi * 1e3,
        'g_tilde_norm': 0.0,
        'gamma_m': 2 * np.pi * 0.8,
        'gamma_o': gamma_o,
        'k': 1,
        'L_p': 9,
        'l': 25,
        'lambda_lc': 589e-9,
        'm': 23,
        'mu': 0.5,
        'N': 1e4,
        'P_lc': 0.2,
        'P_lp_norm': 0.01,
        'R': 12e-6,
        't_approx': 'none',
        't_detuning': '-Omega_m',
        't_line': 's',
        't_offset': 'none',
        't_oss_method': 'cubic',
        't_P_lc': 'norm'
    },
    'plotter': {
        'type': 'lines_3d',
        'x_label': '$\\delta / \\gamma_{o}$',
        'x_label_pad': -2,
        'x_limits': [1.8 * gamma_o, 6.2 * gamma_o],
        'x_tick_labels': [2, '', 6],
        'x_tick_pad': -2,
        'x_ticks': [(i + 1) * 2 * gamma_o for i in range(3)],
        'y_label': '$L_{p}$',
        'y_label_pad': -2,
        'y_limits': [-10.2, 10.2],
        'y_tick_labels': [-10, -5, '', 5, 10],
        'y_tick_pad': -2,
        'y_ticks': [(i - 2) * 5 for i in range(5)],
        'y_colors': ['b', 'r', 'k', 'r', 'b'],
        'y_sizes': [1] * 5,
        'y_styles': ['-'] * 3 + ['--'] * 2,
        'v_label': '$T$',
        'v_label_pad': -12,
        'v_limits': [-0.02, 1.02],
        'v_tick_labels': [0.0, '', 1.0],
        'v_tick_pad': 0,
        'v_ticks': [0.0, 0.5, 1.0],
        'height': 4.8,
        'width': 4.8,
        'view_aspect': [1.0, 1.5, 0.75],
        'view_elevation': 16,
        'view_rotation': -30,
        'annotations': [{
            's': '(a)',
            'xy': (0.03, 0.6)
        }]
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_10, params=params, func='transmission', looper='XYLooper', file_path_prefix='data/v1.1-qom-v0.8.5/3a_0.2P_cr', plot=True)