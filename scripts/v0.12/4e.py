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
        'X': BEC_00.looper_defaults['P_lc'].copy(),
        'Y': BEC_00.looper_defaults['Delta_tilde'].copy(),
    },
    'system': {
        't_detuning': 'val'
    },
    'plotter': {
        'type': 'pcolormesh',
        'palette': 'RdBu',
        'x_label': '$P_{lc}$ (fW)',
        'x_tick_labels': [i * 2 for i in range(3)],
        'x_ticks': [i * 2e-15 for i in range(3)],
        'x_ticks_minor': [i * 1e-15 for i in range(5)],
        'y_label': '$\\tilde{\\Delta} / \\gamma_{o}$',
        'y_label_pad': -18,
        'y_tick_labels': [-2, '', 2],
        'y_ticks': [(i * 2 - 2) * 2 * np.pi * 1e3 for i in range(3)],
        'y_ticks_minor': [(i - 2) * 2 * np.pi * 1e3 for i in range(5)],
        'show_cbar': False,
        'cbar_title': 'Stability Zone',
        'cbar_position': 'top',
        'cbar_tick_labels': ['1U', '1S', '3U', '1S2U', '2S1U', '3S'],
        'cbar_ticks': list(range(6)),
        'annotations': [{
            's': '(e)',
            'xy': (0.15e-15, -1.65 * 2 * np.pi * 1e3)
        }],
        'height': 2.5,
        'width': 2.3
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='osz', looper='XYLooper', file_path_prefix='data/bec_00/osz', plot=True)