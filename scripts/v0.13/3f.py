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
            'min': -20e3,
            'max': 20e3,
            'dim': 40001
        },
        'Y': {
            'var': 'L_p',
            'val': [12, 6, -6, -12]
        }
    },
    'system': {
        't_detuning': 'Omega_n',
        't_offset': 'Omega_n'
    },
    'plotter': {
        'type': 'lines_3d',
        'x_label': '$\\delta - \\Omega_{n}$\n(KHz)',
        'x_label_pad': 6,
        'x_limits': [-22e3, 22e3],
        'x_tick_labels': [-20, '', 20],
        'x_tick_pad': -2,
        'x_ticks': [i * 20e3 - 20e3 for i in range(3)],
        'y_label': '$L_{p}$',
        'y_label_pad': 0,
        'y_limits': [-13.0, -4.5],
        'y_tick_pad': -2,
        'y_ticks': [-12, -6],
        'y_colors': ['y', 'm'],
        'y_sizes': [1] * 2,
        'y_styles': ['-'] * 2,
        'v_label': '$T$',
        'v_label_pad': -12,
        'v_tick_labels': [0.0, '', 2.0],
        'v_tick_pad': 0,
        'v_ticks': [0.0, 1.0, 2.0],
        'height': 3.2,
        'width': 2.3,
        'view_aspect': [1, 0.5, 0.75],
        'view_elevation': 24,
        'view_rotation': -45,
        'annotations': [{
            's': '(f)',
            'xy': (0.057, 0.6)
        }]
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission', looper='XYLooper', file_path_prefix='data/bec_00/v0.13/3e_3f')

# plotter
plotter = MPLPlotter(axes={
    'X': looper.axes['X']['val'],
    'Y': looper.axes['Y']['val'][2:]
}, params=params['plotter'])
plotter.update(vs=looper.results['V'][2:])
plotter.show(hold=True)