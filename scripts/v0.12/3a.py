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
        'X': BEC_00.looper_defaults['L_p'].copy(),
        'Y': {
            'var': 't_offset',
            'val': ['Omega_c', 'Omega_d']
        }
    },
    'system': {
        'G': 2 * np.pi * 1e3,
        't_detuning': 'Omega_m'
    },
    'plotter': {
        'type': 'lines',
        'x_label': '$L_p$',
        'x_label_pad': -16,
        'x_tick_labels': [-12, -6, '', 6, 12],
        'x_ticks': [i * 6 - 12 for i in range(5)],
        'x_ticks_minor': [i * 2 - 12 for i in range(13)],
        'y_colors': ['b', 'r'],
        'y_styles': ['-', '-'],
        'v_label': '$T$',
        'v_label_pad': -22,
        'v_limits': [-0.05, 1.05],
        'v_ticks': [0.0, 1.0],
        'v_ticks_minor': [i * 0.25 for i in range(5)],
        'annotations': [{
            's': '(a)',
            'xy': (-11.5, 0.05)
        }, {
            's': '$\\delta = \\Omega_{c}$',
            'xy': (4.0, 0.75),
            'color': 'b',
            'font_dict': 'tick'
        }, {
            's': '$\\delta = \\Omega_{d}$',
            'xy': (-7.5, 0.75),
            'color': 'r',
            'font_dict': 'tick'
        }],
        'height': 2.0,
        'width': 4.8
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission', looper='XYLooper', file_path_prefix='data/bec_00/transmission_Omega_m_1e3',plot=True)