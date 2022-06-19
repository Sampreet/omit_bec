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

# all parameters
params = {
    'looper': {
        'X': {
            'var': 'P_lc',
            'min': 0e-12,
            'max': 70e-12,
            'dim': 1401
        },
        'Y': {
            'var': 'Delta_tilde',
            'val': [0.5, 1.0, 1.5]
        }
    },
    'system': {
        'G': 2 * np.pi * 7.5e3, 
        'g_tilde_norm': 0.0,
        'gamma_m': 2 * np.pi * 0.8,
        'gamma_o': 2 * np.pi * 2e6,
        'L_p': 1,
        'l': 10,
        'lambda_lc': sc.c / 1e15,
        'm': 23,
        'mu': 1.0,
        'N': 1e4,
        'R': 12e-6,
        't_detuning': 'norm',
        't_oss_method': 'cubic',
        't_P_lc': 'val'
    },
    'plotter': {
        'type': 'scatters',
        'x_name': '$P_{in}$',
        'x_unit': 'pW',
        'x_tick_labels': [i * 10 for i in range(8)],
        'x_ticks': [i * 10e-12 for i in range(8)],
        'x_ticks_minor': [i * 2e-12 for i in range(36)],
        'y_colors': ['b', 'g', 'r'],
        'y_name': '$\\tilde{\\Delta}$',
        'y_unit': '$\\tilde{\\Delta}_{cr}$',
        'y_sizes': [1] * 3,
        'y_styles': ['o'] * 3,
        'v_label': '$\\left| \\alpha_{s} \\right|^{2}$',
        'v_ticks': [i * 5 for i in range(5)],
        'v_ticks_minor': list(range(21)),
        'show_legend': True,
        'legend_location': 'upper left',
        'width': 5.25
    }
}

# looper
wrap_looper(SystemClass=BEC_00, params=params, func='N_os', looper='XYLooper', plot=True)