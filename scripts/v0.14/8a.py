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
        't_detuning': 'Omega_n'
    },
    'plotter': {
        'type': 'lines',
        'x_label': '$\\left| L_p \\right|$',
        'x_label_pad': -16,
        'x_tick_labels': [6, '', 12],
        'x_ticks': [i * 3 + 6 for i in range(3)],
        'y_colors': ['g', 'r', 'm', 'c'],
        'y_styles': ['-', '-', '--', '--'],
        'v_label': '$T$',
        'v_label_pad': -20,
        'v_limits': [-0.125, 1.125],
        'v_tick_labels': [0.0, '', 1.0],
        'v_ticks': [i * 0.5 for i in range(3)],
        'v_ticks_minor': [i * 0.25 for i in range(5)],
        'height': 2.5,
        'width': 2.3,
        'annotations': [{
            's': '(a)',
            'xy': (0.26, 0.82)
        }]
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission', looper='XYZLooper', file_path_prefix='data/bec_00/v0.14/8a')
xs = looper.axes['Y']['val']
vs = [[col[int(len(col) / 2)] for col in row] for row in looper.results['V']]

# plotter
plotter = MPLPlotter(axes={
    'X': xs,
    'Y': ['Omega_c', 'Omega_d', 'Omega_c', 'Omega_d']
}, params=params['plotter'])
plotter.update(xs=xs, vs=vs + [np.flip(v).tolist() for v in vs])
plotter.show(hold=True)