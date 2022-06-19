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
            'var': 'Delta_tilde',
            'min': - 2 * 2 * np.pi * 1e3,
            'max': 2 * 2 * np.pi * 1e3,
            'dim': 1001,
            'scale': 'linear'
        },
        'Y': {
            'var': 'P_lc',
            'min': 0.0,
            'max': 4e-15,
            'dim': 1001,
            'scale': 'linear'
        },
    },
    'system': {
        't_detuning': 'val'
    },
    'plotter': {
        'type': 'pcolormesh',
        'palette': 'RdBu',
        'x_label': '$\\tilde{\\Delta} / \\gamma_{o}$',
        'x_label_pad': -18,
        'x_tick_labels': [-2, '', 2],
        'x_ticks': [(i * 2 - 2) * 2 * np.pi * 1e3 for i in range(3)],
        'x_ticks_minor': [(i - 2) * 2 * np.pi * 1e3 for i in range(5)],
        'y_label': '$P_{lc}$ (fW)',
        'y_label_pad': -14,
        'y_tick_labels': [0, '', 4],
        'y_ticks': [i * 2e-15 for i in range(3)],
        'y_ticks_minor': [i * 1e-15 for i in range(5)],
        'v_ticks': list(range(6)),
        'annotations': [{
            's': '(d)',
            'xy': (0.05, 0.1)
        }, {
            's': 's',
            'xy': (0.48, 0.52),
            'color': 'k',
            'font_dict': 'tick'
        }, {
            's': 'u',
            'xy': (0.76, 0.76),
            'color': 'w',
            'font_dict': 'tick'
        }],
        'height': 2.0,
        'width': 2.3
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='osz', looper='XYLooper', file_path_prefix='data/bec_00/v0.13/3d', plot=True)