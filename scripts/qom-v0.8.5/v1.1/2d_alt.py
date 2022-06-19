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

# frequently used variables
gamma_o = 2 * np.pi * 1e3

# all parameters
params = {
    'looper': {
        'X': {
            'var': 'Delta_tilde',
            'min': - 4 * gamma_o,
            'max': 4 * gamma_o,
            'dim': 1001,
            'scale': 'linear'
        },
        'Y': {
            'var': 'P_lc',
            'min': 0.0,
            'max': 16e-15,
            'dim': 1001,
            'scale': 'linear'
        },
    },
    'system': {
        'Delta_tilde': 0.0,
        'delta_offset': 0.0,
        'G': 2 * np.pi * 1e3,
        'g_tilde_norm': 0.0,
        'gamma_m': 2 * np.pi * 0.8,
        'gamma_o': gamma_o,
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
        't_detuning': 'val',
        't_line': 's',
        't_offset': 'Omega_m',
        't_oss_method': 'cubic',
        't_P_lc': 'val'
    },
    'plotter': {
        'type': 'pcolormesh',
        'palette': 'RdBu',
        'x_label': '$\\tilde{\\Delta} / \\gamma_{o}$',
        'x_label_pad': -32,
        'x_tick_labels': [-4, '', '', '', 4],
        'x_tick_pad': 16,
        'x_ticks': [(i - 2) * 2 * gamma_o for i in range(5)],
        'x_ticks_minor': [(i - 4) * gamma_o for i in range(9)],
        'y_label': '$P_{lc}$ (fW)',
        'y_label_pad': -32,
        'y_tick_labels': [0, '', '', '', 16],
        'y_tick_pad': 16,
        'y_ticks': [i * 4e-15 for i in range(5)],
        'y_ticks_minor': [i * 2e-15 for i in range(9)],
        'v_ticks': list(range(6)),
        'annotations': [{
            's': '(d)',
            'xy': (0.23, 0.8),
            'color': 'k'
        }, {
            's': 'b',
            'xy': (0.28, 0.6),
            'color': 'k',
            'font_dict': 'tick'
        }, {
            's': 's',
            'xy': (0.28, 0.34),
            'color': 'k',
            'font_dict': 'tick'
        }, {
            's': 'u',
            'xy': (0.64, 0.56),
            'color': 'w',
            'font_dict': 'tick'
        }],
        'label_font_size': 40.0,
        'tick_font_size': 32.0,
        'height': 4.0,
        'width': 4.6
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='osz', looper='XYLooper', file_path_prefix='data/v1.1/2d_alt', plot=True)