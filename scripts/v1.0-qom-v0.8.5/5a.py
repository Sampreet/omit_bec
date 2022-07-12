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
            'min': -20e3,
            'max': 20e3,
            'dim': 40001
        },
        'Y': {
            'var': 'L_p',
            'val': [0, 3, 6, 9, 12]
        }
    },
    'system': {
        'G': 2 * np.pi * 1e3,
        't_detuning': 'Omega_n',
        't_offset': 'Omega_n'
    },
    'plotter': {
        'type': 'lines_3d',
        'x_label': '$\\delta - \\Omega_{n}$\n(KHz)',
        'x_label_pad': 12,
        'x_tick_labels': [-20, 0, 20],
        'x_tick_pad': 0,
        'x_ticks': [i * 20e3 - 20e3 for i in range(3)],
        'y_label': '$L_{p}$',
        'y_label_pad': 6,
        'y_tick_pad': 0,
        'y_ticks': [i * 3 for i in range(5)],
        'y_colors': ['k', 'y', 'c', 'g', 'b'],
        'y_sizes': [1] * 5,
        'y_styles': ['-'] * 5,
        'v_label': '$T$',
        'v_label_pad': -12,
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
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission', looper='XYLooper', file_path_prefix='data/v1.0-qom-v0.8.5/5a', plot=True)