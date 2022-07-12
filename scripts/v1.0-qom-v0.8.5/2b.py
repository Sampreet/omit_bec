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
            'var': 'Delta_tilde',
            'min': - 2 * 2 * np.pi * 1e3,
            'max': 2 * 2 * np.pi * 1e3,
            'dim': 401,
            'scale': 'linear'
        },
        'Y': {
            'var': 'P_lc',
            'val': [0.5e-15, 1e-15, 2e-15]
        }
    },
    'system': {
        'G': 2 * np.pi * 1e3,
        't_detuning': 'val'
    },
    'plotter': {
        'type': 'scatters',
        'x_label': '$\\tilde{\\Delta} / \\gamma_{o}$',
        'x_label_pad': -18,
        'x_tick_labels': [-2, '', 2],
        'x_ticks': [(i * 2 - 2) * 2 * np.pi * 1e3 for i in range(3)],
        'x_ticks_minor': [(i - 2) * 2 * np.pi * 1e3 for i in range(5)],
        'y_colors': ['c', 'b', 'r'],
        'y_sizes': [1, 1, 1],
        'y_styles': ['o', 'o', 'o'],
        'v_label': '$N_{o}$',
        'v_label_pad': -12,
        'v_tick_labels': [0, '', 2],
        'v_ticks': [i * 1 for i in range(3)],
        'v_ticks_minor': [i * 0.5 for i in range(5)],
        'annotations': [{
            's': '(b)',
            'xy': (0.76, 0.76)
        }],
        'height': 2.0,
        'width': 2.3
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='moo', looper='XYLooper', plot=True)