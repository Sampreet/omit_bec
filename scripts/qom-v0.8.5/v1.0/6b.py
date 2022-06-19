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
        'x_label': '$\\left| L_{p} \\right|$',
        'x_label_pad': -14,
        'x_tick_labels': [0, 5, '', 15, 20],
        'x_ticks': [i * 5 for i in range(5)],
        'x_ticks_minor': [i * 2.5 for i in range(9)],
        'y_colors': ['b', 'k'],
        'y_styles': ['-', '--'],
        'v_label': '$d T$',
        'v_label_pad': -20,
        'v_limits': [-0.125, 1.125],
        'v_tick_labels': [0.0, '', 1.0],
        'v_ticks': [i * 0.5 for i in range(3)],
        'v_ticks_minor': [i * 0.25 for i in range(5)],
        'height': 2.4,
        'width': 4.8,
        'annotations': [{
            's': '(b)',
            'xy': (0.855, 0.8)
        }, {
            's': 'unresolved\nsideband',
            'xy': (0.18, 0.4),
            'color': 'w',
            'font_dict': 'tick',
            'rotation': 'vertical'
        }]
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission', looper='XYLooper', file_path_prefix='data/v1.0/6')
_dim = len(looper.axes['X']['val'])
xs = looper.axes['Y']['val']
vs = looper.results['V']

# differentiate
vs_diff_stable = [vs[len(xs) - i - 1][int(_dim / 2)] - vs[i][int(_dim / 2)]  if xs[i] >= 5 else np.nan for i in range(len(xs))]
vs_diff_unstable = [vs[len(xs) - i - 1][int(_dim / 2)] - vs[i][int(_dim / 2)] if xs[i] < 5 else np.nan for i in range(len(xs))]

# plotter
plotter = MPLPlotter(axes={
    'X': xs,
    'Y': ['Omega_d', 'Omega_d']
}, params=params['plotter'])
plotter.update(xs=xs, vs=[vs_diff_stable, vs_diff_unstable])
ax = plotter.get_current_axis()
# mark regions
ax.axvspan(-5, 5, facecolor='k', alpha=0.5)
plotter.show(hold=True)