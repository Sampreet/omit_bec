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
            'max': 25e-15,
            'dim': 101,
            'scale': 'linear'
        },
        'Y': {
            'var': 'L_p',
            'val': [9, 0, -9]
        }
    },
    'system': {
        'G': 2 * np.pi * 1e3,
        't_detuning': 'Omega_n'
    },
    'plotter': {
        'type': 'scatters',
        'x_label': '$P_{lc}$ (fW)',
        'x_label_pad': -14,
        'x_tick_labels': [0, '', 25],
        'x_ticks': [i * 12.5e-15 for i in range(3)],
        'x_ticks_minor': [i * 6.25e-15 for i in range(5)],
        'y_colors': ['b', 'k', 'r'],
        'y_sizes': [1, 1, 1],
        'y_styles': ['o', 'o', 'o'],
        'v_label': '$N_{o}$',
        'v_label_pad': -12,
        'v_tick_labels': [0, '', 8],
        'v_ticks': [i * 4 for i in range(3)],
        'v_ticks_minor': [i * 2 for i in range(5)],
        'annotations': [{
            's': '(a)',
            'xy': (0.23, 0.76)
        }],
        'height': 2.0,
        'width': 2.3
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='moo', looper='XYLooper', plot=True)