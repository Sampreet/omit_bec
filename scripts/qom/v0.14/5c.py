# dependencies
import numpy as np
import os 
import sys

# qom modules
from qom.ui.plotters import MPLPlotter
from qom.utils.looper import wrap_looper

# add path to local libraries
sys.path.append(os.path.abspath(os.path.join('..', 'bec-systems')))
# import system
from systems import BEC_00

# all parameters
params = {
    'looper': {
        'grad': True,
        'X': {
            'var': 'delta_offset',
            'min': -0.001,
            'max': 0.001,
            'dim': 101,
            'scale': 'linear'
        },
        'Y': {
            'var': 'L_p',
            'min': -12,
            'max': 12,
            'dim': 1201,
            'scale': 'linear'
        },
        'Z': {
            'var': 't_offset',
            'val': ['Omega_c', 'Omega_d']
        }
    },
    'system': {
        't_detuning': 'Omega_m'
    },
    'plotter': {
        'type': 'lines',
        'x_label': '$L_p$',
        'x_label_pad': -16,
        'x_tick_labels': [-12, '', 12],
        'x_ticks': [i * 12 - 12 for i in range(3)],
        'y_colors': ['g', 'r', 'm', 'c'],
        'y_styles': ['-', '-', '--', '--'],
        'v_label': '$\\tau$ (s)',
        'v_label_pad': -20,
        'v_limits': [-0.05, 0.35],
        'v_tick_labels': [0.0, '', '', 0.3],
        'v_ticks': [0.0, 0.1, 0.2, 0.3],
        'v_ticks_minor': [i * 0.05 for i in range(9)],
        'height': 2.5,
        'width': 2.3,
        'annotations': [{
            's': '(c)',
            'xy': (0.27, 0.82)
        }]
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission_phase', looper='XYZLooper', file_path_prefix='data/bec_00/v0.14/5c')
xs = looper.axes['Y']['val']
vs_neg = [[row[i][int(len(row[i]) / 2)] if xs[i] <= 0 else np.nan for i in range(len(row))] for row in looper.results['V']]
vs_pos = [[row[i][int(len(row[i]) / 2)] if xs[i] >= 0 else np.nan for i in range(len(row))] for row in looper.results['V']]

# plotter
plotter = MPLPlotter(axes={
    'X': xs,
    'Y': ['Omega_c', 'Omega_d', 'Omega_c', 'Omega_d']
}, params=params['plotter'])
plotter.update(xs=xs, vs=vs_pos + vs_neg)
plotter.show(hold=True)