# dependencies
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
        't_detuning': 'Omega_n'
    },
    'plotter': {
        'type': 'lines',
        'x_label': '$L_p$',
        'x_label_pad': -16,
        'x_tick_labels': [6, '', 12],
        'x_ticks': [i * 3 + 6 for i in range(3)],
        'y_colors': ['b', 'r'],
        'y_styles': ['-', '-'],
        'v_label': '',
        'v_label_pad': -20,
        'v_limits': [-0.15, 0.35],
        'v_tick_labels': ['', ''],
        'v_ticks': [-0.1, 0.3],
        'v_ticks_minor': [i * 0.1 - 0.1 for i in range(4)],
        'height': 2.5,
        'width':1.4,
        'annotations': [{
            's': '(c)',
            'xy': (0.54, 0.82)
        }]
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission_phase', looper='XYZLooper', file_path_prefix='data/bec_00/v0.13/5b-5c')
xs = looper.axes['Y']['val']

# plotter
plotter = MPLPlotter(axes={
    'X': xs,
    'Y': ['Omega_c', 'Omega_d']
}, params=params['plotter'])
plotter.update(xs=xs, vs=[[col[int(len(col) / 2)] for col in row] for row in looper.results['V']])
plotter.show(hold=True)