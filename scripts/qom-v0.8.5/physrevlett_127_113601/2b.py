# dependencies
import numpy as np
import os
import scipy.constants as sc
import sys

# qom modules
from qom.utils import wrap_looper

# add path to local libraries
sys.path.append(os.path.abspath(os.path.join('..', 'bec-systems')))
# import system
from systems import BEC_00

# frequently used variables
gamma_o = 2 * np.pi * 2e6

# all parameters
params = {
    'looper': {
        'X': {
            'var': 'Delta_tilde',
            'min': - 3 * gamma_o,
            'max': 3 * gamma_o,
            'dim': 1201
        },
        'Y': {
            'var': 'P_lc',
            'val': [0.25, 1.0, 2.25]
        }
    },
    'system': {
        'G': 2 * np.pi * 7.5e3, 
        'g_tilde_norm': 0.0,
        'gamma_m': 2 * np.pi * 0.8,
        'gamma_o': gamma_o,
        'L_p': 1,
        'l': 10,
        'lambda_lc': sc.c / 1e15,
        'm': 23, 
        'mu': 1.0,
        'N': 1e4,
        'R': 12e-6,
        't_detuning': 'val',
        't_oss_method': 'cubic',
        't_P_lc': 'norm'
    },
    'plotter': {
        'type': 'scatters',
        'x_label': '$\\tilde{\\Delta} / \\gamma_{o}$',
        'x_tick_labels': [(i - 3)  for i in range(7)],
        'x_ticks': [(i - 3) * gamma_o for i in range(7)],
        'x_ticks_minor': [(i - 15) * gamma_o / 5 for i in range(31)],
        'y_colors': ['b', 'g', 'r'],
        'y_name': '$P_{in}$',
        'y_unit': '$P_{cr}$',
        'y_sizes': [1] * 3,
        'y_styles': ['o'] * 3,
        'v_label': '$\\left| \\alpha_{s} \\right|^{2}$',
        'v_ticks': [i * 5 for i in range(5)],
        'v_ticks_minor': list(range(21)),
        'show_legend': True,
        'legend_location': 'upper right',
        'width': 5.25
    }
}

# looper
wrap_looper(SystemClass=BEC_00, params=params, func='N_os', looper='XYLooper', plot=True)