# dependencies
import numpy as np
import os 
import sys

# qom modules
from qom.utils import wrap_looper

# add path to local libraries
sys.path.append(os.path.abspath(os.path.join('..', 'bec-systems')))
# import system
from systems import BEC_00

# all parameters
params = {
    'looper': {
        'X': {
            'var': 'P_lc',
            'min': 0.0,
            'max': 100e-15,
            'dim': 1001,
            'scale': 'linear'
        },
        'Y': {
            'var': 'g_tilde_norm',
            'min': 0.0,
            'max': 40.0,
            'dim': 3,
            'scale': 'linear'
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
        't_detuning': '-Omega_m',
        't_line': 's',
        't_offset': 'Omega_m',
        't_oss_method': 'cubic',
        't_P_lc': 'val'
    },
    'plotter': {
        'type': 'scatters',
        'x_label': '$P_{lc}$ (fW)',
        'x_label_pad': -32,
        'x_tick_labels': [0, '', 100],
        'x_tick_pad': 16,
        'x_ticks': [i * 50e-15 for i in range(3)],
        'x_ticks_minor': [i * 12.5e-15 for i in range(9)],
        'y_colors': ['b', 'g', 'c'],
        'y_sizes': [5, 5, 5],
        'y_styles': ['o', 'o', 'o'],
        'v_label': '$N_{o}$',
        'v_label_pad': -36,
        'v_tick_labels': [0, '', 12],
        'v_tick_pad': 16,
        'v_ticks': [i * 6 for i in range(3)],
        'v_ticks_minor': [i * 2 for i in range(7)],
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
looper = wrap_looper(SystemClass=BEC_00, params=params, func='N_os', looper='XYLooper', plot=True)