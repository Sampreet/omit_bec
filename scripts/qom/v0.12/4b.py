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
            'max': 4e-15,
            'dim': 401,
            'scale': 'linear'
        },
        'Y': BEC_00.looper_defaults['t_detuning'].copy()
    },
    'system': {
        'G': 2 * np.pi * 1e3,
        'g_tilde_norm': 0.0
    },
    'plotter': {
        'type': 'scatters',
        'x_label': '$P_{lc}$ (fW)',
        'x_label_pad': -14,
        'x_tick_labels': [0, '', 4],
        'x_ticks': [i * 2e-15 for i in range(3)],
        'x_ticks_minor': [i * 1e-15 for i in range(5)],
        'y_colors': ['r', 'g', 'b'],
        'y_sizes': [1, 1, 1],
        'y_styles': ['.', 'o', 's'],
        'v_label': '$N_{o}$',
        'v_label_pad': -12,
        'v_tick_labels': [0, '', 2],
        'v_ticks': [i * 1 for i in range(3)],
        'v_ticks_minor': [i * 0.5 for i in range(5)],
        'annotations': [{
            's': '(b)',
            'xy': (0.2e-15, 0.2)
        }],
        'height': 2.0,
        'width': 2.3
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='moo', looper='XYLooper', plot=True)