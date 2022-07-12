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
            'dim': 101,
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
        'G': 2 * np.pi * 1e3,
        't_detuning': 'Omega_m'
    },
    'plotter': {
        'type': 'scatters',
        'x_label': '$P_{lc}$ (fW)',
        'x_label_pad': -14,
        'x_tick_labels': [0, '', 100],
        'x_ticks': [i * 50e-15 for i in range(3)],
        'x_ticks_minor': [i * 25e-15 for i in range(5)],
        'y_colors': ['b', 'g', 'y'],
        'y_sizes': [1, 1, 1],
        'y_styles': ['o', 'o', 'o'],
        'v_label': '$N_{o}$',
        'v_label_pad': -18,
        'v_tick_labels': [0, '', 12],
        'v_ticks': [i * 6 for i in range(3)],
        'v_ticks_minor': [i * 3 for i in range(5)],
        'annotations': [{
            's': '(a)',
            'xy': (0.24, 0.76)
        }],
        'height': 2.0,
        'width': 2.3
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='moo', looper='XYLooper', plot=True)