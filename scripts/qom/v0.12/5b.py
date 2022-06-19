# dependencies
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
        't_detuning': 'Omega_n'
    },
    'plotter': {
        'type': 'lines',
        'x_label': '$L_p$',
        'x_label_pad': -16,
        'x_tick_labels': [6, '', 12],
        'x_ticks': [i * 3 + 6 for i in range(3)],
        'y_colors': ['b', 'r'],
        'y_styles': ['-', '-'],
        'v_label': '$T$',
        'v_label_pad': -22,
        'v_limits': [0.1, 1.1],
        'v_ticks': [0.2, 1.0],
        'annotations': [{
            's': '(c)',
            'xy': (6.3, 0.175)
        }, {
            's': '$\\delta = \\Omega_{c}$',
            'xy': (8.1, 0.775),
            'color': 'b',
            'font_dict': 'tick'
        }, {
            's': '$\\delta = \\Omega_{d}$',
            'xy': (7.3, 0.5),
            'color': 'r',
            'font_dict': 'tick'
        }],
        'height': 2.5,
        'width': 2.3
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission', looper='XYLooper', file_path_prefix='data/bec_00/transmission_Omega_n',plot=True)