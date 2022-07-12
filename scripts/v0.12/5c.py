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
            'min': -10,
            'max': 10,
            'dim': 10001,
            'scale': 'linear'
        },
        'Y': BEC_00.looper_defaults['L_p'].copy(),
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
        'v_label': '$\\tau$ (s)',
        'v_label_pad': -24,
        'v_limits': [-0.15, 0.05],
        'v_ticks': [-0.1, 0.0],
        'annotations': [{
            's': '(b)',
            'xy': (-11.75, -0.135)
        }, {
            's': '$\\delta = \\Omega_{c}$',
            'xy': (-9.4, -0.14),
            'color': 'b',
            'font_dict': 'tick'
        }, {
            's': '$\\delta = \\Omega_{d}$',
            'xy': (-9.9, 0.01),
            'color': 'r',
            'font_dict': 'tick'
        }],
        'height': 2.5,
        'width': 2.3
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission_phase', looper='XYZLooper', file_path_prefix='data/bec_00/group_delay_Omega_n')
xs = looper.axes['Y']['val']

# plotter
plotter = MPLPlotter(axes={
    'X': xs,
    'Y': ['Omega_c', 'Omega_d']
}, params=params['plotter'])
plotter.update(xs=xs, vs=[[col[int(len(col) / 2)] for col in row] for row in looper.results['V']])
plotter.show(hold=True)