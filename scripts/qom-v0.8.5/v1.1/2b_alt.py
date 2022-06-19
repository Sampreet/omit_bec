# dependencies
import numpy as np
import os 
import sys

# qom modules
from qom.utils import wrap_looper

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
            'val': [0.25, 1.0, 2.25]
        }
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
        't_P_lc': 'norm'
    },
    'plotter': {
        'type': 'scatters',
        'x_label': '$\\tilde{\\Delta} / \\gamma_{o}$',
        'x_label_pad': -32,
        'x_tick_labels': [-4, '', '', '', 4],
        'x_tick_pad': 16,
        'x_ticks': [(i - 2) * 2 * gamma_o for i in range(5)],
        'x_ticks_minor': [(i - 4) * gamma_o for i in range(9)],
        'y_colors': ['b', 'g', 'r'],
        'y_sizes': [5, 5, 5],
        'y_styles': ['o', 'o', 'o'],
        'y_unit': '$P_{\\mathrm{cr}}$',
        'v_label': '$N_{o}$',
        'v_label_pad': -24,
        'v_tick_labels': [0, '', '', '', 4],
        'v_tick_pad': 16,
        'v_ticks': [i for i in range(5)],
        'v_ticks_minor': [i * 0.5 for i in range(9)],
        'show_legend': True,
        'annotations': [{
            's': '(b)',
            'xy': (0.2, 0.8)
        }],
        'legend_font_size': 24.0,
        'label_font_size': 40.0,
        'tick_font_size': 32.0,
        'height': 4.0,
        'width': 4.6
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='N_os', looper='XYLooper', plot=True)