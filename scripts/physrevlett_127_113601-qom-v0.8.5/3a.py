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
            'var': 'delta_offset',
            'min': 2 * np.pi * 500,
            'max': 2 * np.pi * 700,
            'dim': 201
        }
    },
    'system': {
        'Delta_tilde': 0.0,
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
        'P_lc': 12.4e-15,
        'R': 12e-6,
        't_detuning': 'norm',
        't_offset': 'val',
        't_oss_method': 'basic',
        't_P_lc': 'val'
    },
    'plotter': {
        'type': 'lines',
        'x_name': '$\\omega / ( 2 \\pi )$',
        'x_unit': 'Hz',
        'x_tick_labels': [500, 550, 600, 650, 700],
        'x_ticks': [i * 2 * np.pi * 50 + 2 * np.pi * 500 for i in range(5)],
        'x_ticks_minor': [i * 2 * np.pi * 10 + 2 * np.pi * 500 for i in range(21)],
        'v_name': '$S( \\omega )$',
        'v_scale': 'log',
        'v_tick_labels': ['$10^{-2}$', '$10^{-1}$', '$10^{0}$'],
        'v_ticks': [0.01, 0.1, 1],
        'v_ticks_minor': [i * 0.01 + 0.01 for i in range(9)] + [i * 0.1 + 0.1 for i in range(10)],
        'v_unit': '1/Hz',
        'width': 5.25
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='Ss', looper='XLooper')
xs = looper.results['X']
vs = [v[0] + v[1] + v[2] for v in looper.results['V']]

# plotter
plotter = MPLPlotter(axes={
    'X': xs
}, params=params['plotter'])
plotter.update(xs=xs, vs=vs)
plotter.show(hold=True)