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
            'min': -100,
            'max': 100,
            'dim': 1001
        },
        'Y': {
            'var': 'L_p',
            'val': [-9, 9]
        },
        'Z': BEC_00.looper_defaults['g_tilde_norm'].copy()
    },
    'system': {
        'G': 2 * np.pi * 1e3,
        't_detuning': 'Omega_m',
        't_offset': 'Omega_d'
    },
    'plotter': {
        'type': 'lines',
        'x_label': '$\\delta - \\Omega_{d}$ (Hz)',
        'x_ticks': [i * 100 - 100 for i in range(3)], 
        'y_colors': ['r', 'b'] * 3,
        'y_styles': ['-', '-', '-.', '-.', ':', ':'],
        'v_label': '',
        'v_limits': [-0.05, 1.05],
        'v_tick_labels': ['', ''],
        'v_ticks': [0.0, 1.0],
        'v_ticks_minor': [i * 0.25 for i in range(5)],
        'annotations': [{
            's': '(c)',
            'xy': (-85.0, 0.05)
        }],
        'height': 2.5,
        'width': 1.6
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission', looper='XYZLooper')
xs = looper.axes['X']['val']

# plotter
plotter = MPLPlotter(axes={
    'X': xs,
    'Y': [-9, 9, -9, 9, -9, 9]
}, params=params['plotter'])
plotter.update(xs=xs, vs=looper.results['V'][0] + looper.results['V'][1] + looper.results['V'][2])
plotter.show(hold=True)