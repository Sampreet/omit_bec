# dependencies
import numpy as np
import os 
import sys

# qom modules
from qom.utils.looper import wrap_looper

# add path to local libraries
sys.path.append(os.path.abspath(os.path.join('..', 'bec-systems')))
# import system
from systems import BEC_10

# all parameters
params = {
    'looper': {
        'X': {
            'var': 'P_lc',
            'min': 0.0,
            'max': 16e-15,
            'dim': 1001,
            'scale': 'linear'
        },
        'Y': {
            'var': 'L_p',
            'min': -10,
            'max': 10,
            'dim': 1001,
            'scale': 'linear'
        }
    },
    'system': {
        'Delta_tilde': 0.0,
        'delta_offset': 0.0,
        'G': 2 * np.pi * 1e3,
        'g_tilde_norm': 0.0,
        'gamma_m': 2 * np.pi * 0.8,
        'gamma_o': 2 * np.pi * 1e3,
        'k': 1,
        'L_p': 9,
        'l': 25,
        'lambda_lc': 589e-9,
        'm': 23,
        'mu': 0.5,
        'N': 1e4,
        'P_lc': 0.05,
        'P_lp_norm': 0.01,
        'R': 12e-6,
        't_approx': 'none',
        't_detuning': '-Omega_m',
        't_line': 's',
        't_offset': 'Omega_m',
        't_oss_method': 'cubic',
        't_P_lc': 'val'
    },
    'plotter': {
        'type': 'pcolormesh',
        'palette': 'RdBu',
        'x_label': '$P_{lc}$ (fW)',
        'x_label_pad': -32,
        'x_tick_labels': [0, '', '', '', 16],
        'x_tick_pad': 16,
        'x_ticks': [i * 4e-15 for i in range(5)],
        'x_ticks_minor': [i * 2e-15 for i in range(9)],
        'y_label': '$L_{p}$',
        'y_label_pad': -48,
        'y_tick_labels': [-10, '', '', '', 10],
        'y_tick_pad': 16,
        'y_ticks': [(i - 2) * 5 for i in range(5)],
        'y_ticks_minor': [(i - 4) * 2.5 for i in range(9)],
        'v_ticks': list(range(6)),
        'annotations': [{
            's': '(c)',
            'xy': (0.76, 0.8)
        }, {
            's': 's',
            'xy': (0.36, 0.54),
            'color': 'k',
            'font_dict': 'tick'
        }, {
            's': 'b',
            'xy': (0.70, 0.54),
            'color': 'k',
            'font_dict': 'tick'
        }],
        'label_font_size': 40.0,
        'tick_font_size': 32.0,
        'height': 4.0,
        'width': 4.6
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_10, params=params, func='osz', looper='XYLooper', file_path_prefix='data/v1.1-qom-v0.8.5/2c_alt', plot=True)