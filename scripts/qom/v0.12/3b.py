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
            'min': -0.01,
            'max': 0.01,
            'dim': 101,
            'scale': 'linear'
        },
        'Y': BEC_00.looper_defaults['L_p'].copy(),
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
        'x_tick_labels': [-12, -6, '', 6, 12],
        'x_ticks': [i * 6 - 12 for i in range(5)],
        'x_ticks_minor': [i * 2 - 12 for i in range(13)],
        'y_colors': ['b', 'r'],
        'y_styles': ['-', '-'],
        'v_label': '$\\tau$ (s)',
        'v_label_pad': -24,
        'v_limits': [-0.05, 0.35],
        'v_ticks': [0.0, 0.3],
        'annotations': [{
            's': '(a)',
            'xy': (-11.5, -0.015)
        }, {
            's': '$\\delta = \\Omega_{c}$',
            'xy': (-7.0, 0.05),
            'color': 'b',
            'font_dict': 'tick'
        }, {
            's': '$\\delta = \\Omega_{d}$',
            'xy': (3.5, 0.05),
            'color': 'r',
            'font_dict': 'tick'
        }],
        'height': 2.0,
        'width': 4.8
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission_phase', looper='XYZLooper')
xs = looper.axes['Y']['val']

# plotter
plotter = MPLPlotter(axes={
    'X': xs,
    'Y': ['Omega_c', 'Omega_d']
}, params=params['plotter'])
plotter.update(xs=xs, vs=[[col[int(len(col) / 2)] for col in row] for row in looper.results['V']])
plotter.show(hold=True)