# dependencies
import numpy as np
import os 
import sys

# qom modules
from qom.utils import wrap_looper

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
            'max': 5e-15,
            'dim': 1001,
            'scale': 'linear'
        },
        'Y': {
            'var': 'Delta_tilde',
            'val': [0.5, 1.0, 1.5]
        }
    },
    'system': {
        'Delta_tilde': 0.0,
        'delta_offset': 0.0,
        'G': 2 * np.pi * 1e3,
        'g_tilde_norm': 0.0,
        'gamma_m': 2 * np.pi * 0.8,
        'gamma_o': 2 * np.pi * 1e3,
        'k': 1,
        'L_p': 9,
        'l': 25,
        'lambda_lc': 589e-9,
        'm': 23,
        'mu': 0.5,
        'N': 1e4,
        'P_lc': 0.05,
        'P_lp_norm': 0.01,
        'R': 12e-6,
        't_approx': 'none',
        't_detuning': 'norm',
        't_line': 's',
        't_offset': 'Omega_m',
        't_oss_method': 'cubic',
        't_P_lc': 'val'
    },
    'plotter': {
        'type': 'scatters',
        'x_label': '$P_{lc}$ (fW)',
        'x_label_pad': -32,
        'x_tick_labels': [0, '', '', '', '', 5],
        'x_tick_pad': 16,
        'x_ticks': [i * 1e-15 for i in range(6)],
        'x_ticks_minor': [i * 0.5e-15 for i in range(11)],
        'y_colors': ['b', 'g', 'r'],
        'y_sizes': [5, 5, 5],
        'y_styles': ['o', 'o', 'o'],
        'v_label': '$N_{o}$',
        'v_label_pad': -24,
        'v_tick_labels': [0, '', '', 3],
        'v_tick_pad': 16,
        'v_ticks': [i for i in range(4)],
        'v_ticks_minor': [i * 0.5 for i in range(7)],
        'annotations': [{
            's': '(a)',
            'xy': (0.2, 0.8)
        }],
        'label_font_size': 40.0,
        'tick_font_size': 32.0,
        'height': 4.0,
        'width': 4.6
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_10, params=params, func='N_os', looper='XYLooper', plot=True)