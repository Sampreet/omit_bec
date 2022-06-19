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

# frequently used variables
gamma_o = 2 * np.pi * 0.1e6

# all parameters
params = {
    'looper': {
        'X': {
            'var': 'delta_offset',
            'min': -gamma_o ,
            'max': gamma_o,
            'dim': 10001
        },
        'Y': {
            'var': 'L_p',
            'min': -50 ,
            'max': 50,
            'dim': 101
        },
        'Z': {
            'var': 'l',
            'val': list(range(26, 51, 4))
        }
    },
    'system': {
        'Delta_tilde': 0.0,
        'delta_offset': 0.0,
        'G': 2 * np.pi * 159,
        'g_tilde_norm': 0.0,
        'gamma_m': 2 * np.pi * 0.8,
        'gamma_o': gamma_o,
        'k': 1,
        'L_p': 10,
        'l': 26,
        'lambda_lc': 589e-9,
        'm': 23,
        'mu': 0.5,
        'N': 1e4,
        'P_lc': 0.000004,
        'P_lp_norm': 0.01,
        'R': 12e-6,
        't_approx': 'none',
        't_detuning': '-Omega_n',
        't_line': 's',
        't_offset': 'none',
        't_oss_method': 'cubic',
        't_P_lc': 'norm'
    },
    'plotter': {
        'type': 'lines',
        'x_label': '$\\left| L_{p} \\right|$',
        'x_ticks': [i * 10 for i in range(6)],
        'x_ticks_minor': [i * 2 for i in range(26)],
        'y_colors': ['k', 'm', 'r', 'y', 'g', 'c', 'b'],
        'y_name': '$l$',
        'y_sizes': [1] * 7,
        'y_styles': ['-'] * 7,
        'v_label': '$T_{-} - T_{+}$',
        'v_tick_labels': ['{:1.1f}'.format(i * 0.1) for i in range(7)],
        'v_ticks': [i * 0.1 for i in range(7)],
        'v_ticks_minor': [i * 0.05 for i in range(13)],
        'show_legend': True,
        'legend_location': 'upper left',
        'legend_font_size': 12.0,
        'height': 4.0,
        'width': 4.8,
        'annotations': [{
            's': '(b)',
            'xy': (0.55, 0.86)
        }]
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission', looper='XYZLooper', file_path_prefix='data/v1.1/7')

# frequently used variables
xs = looper.axes['X']['val']
ys = looper.axes['Y']['val']
V = looper.results['V']

# find dip positions
dips = [[int(np.argwhere(V[i][j] == np.min(V[i][j]))[0]) for j in range(len(V[i]))] for i in range(len(V))]

# find difference in transparencies
T_diff = [[V[i][50 - j][dips[i][50 + j]] for j in range(51)] for i in range(len(V))]

# plotter
plotter = MPLPlotter(axes={
    'X': ys[50:],
    'Y': list(range(26, 51, 4))
}, params=params['plotter'])
plotter.update(xs=ys[50:], vs=T_diff)
plotter.show(hold=True)