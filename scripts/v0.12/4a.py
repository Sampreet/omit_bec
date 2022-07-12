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
            'min': -10e3,
            'max': 10e3,
            'dim': 1001
        },
        'Y': {
            'var': 'L_p',
            'val': [0, 3, 6, 9]
        },
        'Z': BEC_00.looper_defaults['g_tilde_norm'].copy()
    },
    'system': {
        'G': 2 * np.pi * 1e3,
        't_detuning': 'Omega_n',
        't_offset': 'Omega_n'
    },
    'plotter': {
        'type': 'lines',
        'x_label': '$\\delta - \\Omega_{n}$ (KHz)',
        'x_label_pad': -16,
        'x_tick_labels': [-10, -6, '', '', 6, 10],
        'x_ticks': [i * 4e3 - 10e3 for i in range(6)],
        'x_ticks_minor': [i * 2e3 - 10e3 for i in range(11)],  
        'y_colors': ['k', 'y', 'g', 'b'] * 3,
        'y_styles': ['-', '-', '-', '-', '-.', '-.', '-.', '-.', ':', ':', ':', ':'],
        'v_label': '$T$',
        'v_label_pad': -22,
        'v_limits': [-0.05, 1.05],
        'v_ticks': [0.0, 1.0],
        'v_ticks_minor': [i * 0.25 for i in range(5)],
        'annotations': [{
            's': '(a)',
            'xy': (-9750.0, 0.05)
        }, {
            's': '$6$',
            'xy': (8200.0, 0.25),
            'color': 'g',
            'font_dict': 'tick'
        }, {
            's': '$0$',
            'xy': (-7100.0, 0.25),
            'color': 'k',
            'font_dict': 'tick'
        }, {
            's': '$3$',
            'xy': (500.0, 0.25),
            'color': 'y',
            'font_dict': 'tick'
        }, {
            's': '$9$',
            'xy': (2500.0, 0.25),
            'color': 'b',
            'font_dict': 'tick'
        }],
        'height': 2.0,
        'width': 4.8
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission', looper='XYZLooper')
xs = looper.axes['X']['val']

# plotter
plotter = MPLPlotter(axes={
    'X': xs,
    'Y': [0, 3, 6, 9] * 3
}, params=params['plotter'])
plotter.update(xs=xs, vs=looper.results['V'][0] + looper.results['V'][1] + looper.results['V'][2])
plotter.show(hold=True)