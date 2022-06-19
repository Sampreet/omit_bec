# dependencies
import numpy as np
import os 
import scipy.constants as sc
import sys

# qom modules
from qom.ui.plotters import MPLPlotter
from qom.utils import wrap_looper

# add path to local libraries
sys.path.append(os.path.abspath(os.path.join('..', 'bec-systems')))
# import system
from systems import BEC_00

# all parameters
params = {
    'looper': {
        'X': {
            'var': 'P_lc',
            'min': -15,
            'max': -15 + np.log10(20),
            'dim': 1001,
            'scale': 'log'
        }
    },
    'system': {
        'Delta_tilde': 0.0,
        'delta_offset': 2 * np.pi * 0.3,
        'G': 2 * np.pi * 7.5e3, 
        'g_tilde_norm': 0.0,
        'gamma_m': 2 * np.pi * 0.8,
        'gamma_o': 2 * np.pi * 2e6,
        'L_p': 1,
        'l': 10,
        'lambda_lc': 589e-9,
        'm': 23,
        'mu': 1.0,
        'N': 1e4,
        'R': 12e-6,
        't_detuning': 'norm',
        't_offset': 'Omega_c',
        't_oss_method': 'basic',
        't_P_lc': 'val'
    },
    'plotter': {
        'type': 'lines',
        'x_name': '$P_{in}$',
        'x_unit': 'fW',
        'x_scale': 'log',
        'x_tick_labels': [1, 5, 10, 20],
        'x_ticks': [1e-15, 5e-15, 10e-15, 20e-15],
        'x_ticks_minor': [i * 1e-15 + 1e-15 for i in range(9)],
        'y_colors': ['r', 'b', 'g', 'k'],
        'y_legend': ['$S_{\\mathrm{sn}}$', '$S_{\\mathrm{rp}}$', '$S_{\\mathrm{th}}$', '$S$'],
        'y_sizes': [2] * 4,
        'y_styles': ['--', '--', '--', '-'],
        'v_name': '$S( \\omega_{\\mathrm{opt}} )$',
        'v_scale': 'log',
        'v_tick_labels': ['$10^{-2}$', '$10^{-1}$', '$10^{0}$'],
        'v_ticks': [0.01, 0.1, 1],
        'v_ticks_minor': [i * 0.01 + 0.01 for i in range(9)] + [i * 0.1 + 0.1 for i in range(10)],
        'v_unit': '1/Hz',
        'show_legend': True,
        'legend_location': 'lower center',
        'width': 5.25
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='Ss', looper='XLooper')
xs = looper.results['X']
vs = np.transpose([[v[0], v[1], v[2], v[0] + v[1] + v[2]] for v in looper.results['V']]).tolist()

# plotter
plotter = MPLPlotter(axes={
    'X': xs
}, params=params['plotter'])
plotter.update(xs=xs, vs=vs)
plotter.show(hold=True)