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
        'x_tick_labels': [-12, '', -6],
        'x_ticks': [i * 3 - 12 for i in range(3)],
        'y_colors': ['b', 'r'],
        'y_styles': ['-', '-'],
        'v_label': '',
        'v_label_pad': -20,
        'v_limits': [-0.05, 1.05],
        'v_tick_labels': ['', ''],
        'v_ticks': [i * 0.5 for i in range(3)],
        'v_ticks_minor': [i * 0.25 for i in range(5)],
        'height': 2.5,
        'width':1.4,
        'annotations': [{
            's': '(b)',
            'xy': (0.26, 0.28)
        }]
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission', looper='XYZLooper', file_path_prefix='data/bec_00/v0.13/4b-4c')
xs = looper.axes['Y']['val']

# plotter
plotter = MPLPlotter(axes={
    'X': xs,
    'Y': ['Omega_c', 'Omega_d']
}, params=params['plotter'])
plotter.update(xs=xs, vs=[[col[int(len(col) / 2)] for col in row] for row in looper.results['V']])
plotter.show(hold=True)