# dependencies
import numpy as np
import os 
import sys

# qom modules
from qom.utils.looper import wrap_looper

# add path to local libraries
sys.path.append(os.path.abspath(os.path.join('..', 'bec-systems')))
# import system
from systems import BEC_00

# all parameters
params = {
    'looper': {
        'X': {
            'var': 'delta_offset',
            'min': -10e3,
            'max': 10e3,
            'dim': 2001
        },
        'Y': {
            'var': 'L_p',
            'val': [0, 3, 6, 9]
        }
    },
    'system': {
        'G': 2 * np.pi * 1e3,
        't_detuning': 'Omega_m',
        't_offset': 'Omega_m'
    },
    'plotter': {
        'type': 'lines_3d',
        'x_label': '$\\delta - \\Omega_{m}$\n(KHz)',
        'x_label_pad': 12,
        'x_tick_labels': [-10, 0, 10],
        'x_tick_pad': 0,
        'x_ticks': [i * 10e3 - 10e3 for i in range(3)],
        'y_label': '$L_{p}$',
        'y_label_pad': 6,
        'y_tick_pad': 0,
        'y_ticks': [i * 3 for i in range(4)],
        'y_colors': ['k', 'y', 'g', 'b'],
        'y_sizes': [1] * 4,
        'y_styles': ['-'] * 4,
        'v_label': '$T$',
        'v_label_pad': -12,
        'v_tick_labels': [0.0, '', 1.0],
        'v_tick_pad': 0,
        'v_ticks': [0.0, 0.5, 1.0],
        'height': 3.2,
        'width': 3.2,
        'view_aspect': [1.0, 1.0, 0.75],
        'view_elevation': 16,
        'view_rotation': -30,
        'annotations': [{
            's': '(e)',
            'xy': (0.05, 0.65)
        }]
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission', looper='XYLooper', plot=True)