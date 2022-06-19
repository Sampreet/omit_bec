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
        'X': BEC_00.looper_defaults['P_lc'].copy(),
        'Y': BEC_00.looper_defaults['L_p'].copy()
    },
    'system': {
        't_detuning': 'Omega_n'
    },
    'plotter': {
        'type': 'pcolormesh',
        'palette': 'RdBu',
        'x_label': '$P_{lc}$ (fW)',
        'x_tick_labels': [i * 2 for i in range(3)],
        'x_ticks': [i * 2e-15 for i in range(3)],
        'x_ticks_minor': [i * 1e-15 for i in range(5)],
        'y_label': '$L_{p}$',
        'y_label_pad': -24,
        'y_tick_labels': [-12, '', 12],
        'y_ticks': [i * 12 - 12 for i in range(3)],
        'y_ticks_minor': [i * 6 - 12 for i in range(5)],
        'show_cbar': False,
        'cbar_title': 'Stability Zone for $\\tilde{\\Delta} = - \\Omega_{n}$',
        'cbar_position': 'top',
        'cbar_tick_labels': ['1U', '1S', '3U', '1S2U', '2S1U', '3S'],
        'cbar_ticks': list(range(6)),
        'annotations': [{
            's': '(d)',
            'xy': (0.15e-15, -10.0)
        }],
        'height': 2.5,
        'width': 2.3
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='osz', looper='XYLooper', file_path_prefix='data/bec_00/osz_Omega_n', plot=True)