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
            'min': -20,
            'max': 20,
            'dim': 4001,
            'scale': 'linear'
        }
    },
    'system': {
        't_detuning': 'Omega_n',
        't_offset': 'Omega_d'
    },
    'plotter': {
        'type': 'lines',
        'x_label': '$L_{p}$',
        'x_ticks': [i * 2 + 5 for i in range(5)],
        'x_ticks_minor': [i + 5 for i in range(8)],
        'y_colors': ['b', 'k', 'r'],
        'y_styles': ['-', '--', '-'],
        'v_label': '$\\tau$ (s)',
        'v_limits': [-0.05, 0.25],
        'v_ticks': [0.0, 0.1, 0.2],
        'v_ticks_minor': [i * 0.05 for i in range(5)],
        'height': 2.4,
        'width': 4.8,
        'annotations': [{
            's': 'I',
            'xy': (0.27, 0.6)
        }, {
            's': 'II',
            'xy': (0.5, 0.6)
        }, {
            's': 'III',
            'xy': (0.78, 0.6)
        }]
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission_phase', looper='XYLooper', file_path_prefix='data/v1.0-qom-v0.8.5/7')
_dim = len(looper.axes['X']['val'])
xs = looper.axes['Y']['val']

# differentiate
vs_stable_m = [looper.results['V'][i][int(_dim / 2)] if xs[i] <= -5 else np.nan for i in range(len(xs))]
vs_stable_p = [looper.results['V'][i][int(_dim / 2)] if xs[i] >= 5 else np.nan for i in range(len(xs))]
vs_unstable = [looper.results['V'][i][int(_dim / 2)] if np.abs(xs[i]) < 5 else np.nan for i in range(len(xs))]

# plotter
plotter = MPLPlotter(axes={
    'X': xs,
    'Y': ['Omega_d', 'Omega_d', 'Omega_d']
}, params=params['plotter'])
ax = plotter.get_current_axis()
ax.plot(xs, np.zeros_like(xs), 'k', linewidth=1)
ax.vlines(x=[6.9, 9.9], ymin=-0.05, ymax=0.25, colors='k', linestyles='dashed', linewidth=1)
plotter.update(xs=xs, vs=[vs_stable_m, vs_unstable, vs_stable_p])
# zero line
plotter.show(hold=True)