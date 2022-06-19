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

# all parameters
params = {
    'looper': {
        'X': {
            'var': 'P_lc',
            'min': 0.0,
            'max': 2e-9,
            'dim': 1001,
            'scale': 'linear'
        },
        'Y': {
            'var': 'Delta_tilde',
            'val': [0.5, 1.0, 1.5]
        }
    },
    'system': {
        'Delta_tilde': 0.0,
        'delta_offset': 0.0,
        'G': 2 * np.pi * 159,
        'g_tilde_norm': 20.0,
        'gamma_m': 2 * np.pi * 0.8,
        'gamma_o': 2 * np.pi * 0.1e6,
        'k': 1,
        'L_p': 10,
        'l': 26,
        'lambda_lc': 589e-9,
        'm': 23,
        'mu': 0.5,
        'N': 1e4,
        'P_lc': 0.05,
        'P_lp_norm': 0.01,
        'R': 12e-6,
        't_approx': 'none',
        't_detuning': 'norm',
        't_line': 's',
        't_offset': 'Omega_n',
        't_oss_method': 'cubic',
        't_P_lc': 'val'
    },
    'plotter': {
        'type': 'scatters',
        'x_label': '$P_{lc}$ (nW)',
        'x_label_pad': -32,
        'x_tick_labels': [0, '', '', '', 2],
        'x_tick_pad': 16,
        'x_ticks': [i * 0.5e-9 for i in range(5)],
        'x_ticks_minor': [i * 0.25e-9 for i in range(9)],
        'y_colors': ['b', 'g', 'r'],
        'y_sizes': [5, 5, 5],
        'y_styles': ['o', 'o', 'o'],
        'y_unit': '$\\tilde{\\Delta}_{\\mathrm{cr}}$',
        'v_label': '$N_{o} / 10^{4}$',
        'v_label_pad': -24,
        'v_tick_labels': [0, '', '', '', 2],
        'v_tick_pad': 16,
        'v_ticks': [i * 0.5e4 for i in range(5)],
        'v_ticks_minor': [i * 0.25e4 for i in range(9)],
        'show_legend': True,
        'annotations': [{
            's': '(a)',
            'xy': (0.77, 0.8)
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