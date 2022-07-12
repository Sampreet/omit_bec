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
        'X': {
            'var': 'P_lc',
            'min': 0.0,
            'max': 10e-15,
            'dim': 1001,
            'scale': 'linear'
        },
        'Y': {
            'var': 'L_p',
            'min': -12,
            'max': 12,
            'dim': 1201,
            'scale': 'linear'
        }
    },
    'system': {
        't_detuning': 'Omega_n'
    },
    'plotter': {
        'type': 'pcolormesh',
        'palette': 'RdBu',
        'x_label': '$P_{lc}$ (fW)',
        'x_label_pad': -14,
        'x_tick_labels': [0, '', 10],
        'x_ticks': [i * 5e-15 for i in range(3)],
        'x_ticks_minor': [i * 2.5e-15 for i in range(5)],
        'y_label': '$L_{p}$',
        'y_label_pad': -24,
        'y_tick_labels': [-12, '', 12],
        'y_ticks': [i * 12 - 12 for i in range(3)],
        'y_ticks_minor': [i * 6 - 12 for i in range(5)],
        'v_ticks': list(range(6)),
        'annotations': [{
            's': '(c)',
            'xy': (0.05, 0.1)
        }, {
            's': 's',
            'xy': (0.48, 0.6),
            'color': 'k',
            'font_dict': 'tick'
        }, {
            's': 'u',
            'xy': (0.76, 0.4),
            'color': 'w',
            'font_dict': 'tick'
        }],
        'height': 2.0,
        'width': 2.3
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='osz', looper='XYLooper', file_path_prefix='data/bec_00/v0.13/3c', plot=True)