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
gamma_o = 2 * np.pi * 1e3

# all parameters
params = {
    'looper': {
        'X': {
            'var': 'delta_offset',
            'min': -2.0 * gamma_o,
            'max': 2.0 * gamma_o,
            'dim': 40001
        },
        'Y': {
            'var': 'L_p',
            'min': -10,
            'max': 10,
            'dim': 101,
            'scale': 'linear'
        }
    },
    'system': {
        'Delta_tilde': 0.0,
        'delta_offset': 0.0,
        'G': 2 * np.pi * 1e3,
        'g_tilde_norm': 0.0,
        'gamma_m': 2 * np.pi * 0.8,
        'gamma_o': gamma_o,
        'k': 1,
        'L_p': 9,
        'l': 25,
        'lambda_lc': 589e-9,
        'm': 23,
        'mu': 0.5,
        'N': 1e4,
        'P_lc': 0.2,
        'P_lp_norm': 0.01,
        'R': 12e-6,
        't_approx': 'none',
        't_detuning': '-Omega_m',
        't_line': 's',
        't_offset': 'Omega_m',
        't_oss_method': 'cubic',
        't_P_lc': 'norm'
    },
    'plotter': {
        'type': 'lines',
        'x_label': '$L_{p}$',
        'x_ticks': [i * 5 - 10 for i in range(5)],
        'x_ticks_minor': [i * 1 - 10 for i in range(21)],
        'y_colors': ['b', 'b'],
        'y_styles': ['--', '-'],
        'v_label': '$d \\delta / \gamma_{o}$',
        'v_tick_labels': [i for i in range(4)],
        'v_ticks': [i * gamma_o for i in range(4)],
        'v_ticks_minor': [i * 0.2 * gamma_o for i in range(16)],
        'height': 3.6,
        'width': 4.8
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission', looper='XYLooper', file_path_prefix='data/v1.1/4_0.2P_cr')

# frequently used variables
xs = looper.axes['X']['val']
ys = looper.axes['Y']['val']
V = looper.results['V']

# get peaks
dpeaks_ddelta = [np.gradient(V[i]) for i in range(len(V))]
peaks = [np.where(np.abs(dpeaks_ddelta[i]) > 1e-2, 1, 0) for i in range(len(dpeaks_ddelta))]
peaks_neg = np.array([[peaks[i][int(len(xs) / 2) - j] for j in range(int(len(xs) / 2) + 1)] for i in range(len(peaks))])
peaks_pos = np.array([[peaks[i][int(len(xs) / 2) + j] for j in range(int(len(xs) / 2) + 1)] for i in range(len(peaks))])

# calculate differences
vs = list()
for i in range(len(peaks)):
    peak_neg = np.where(peaks_neg[i] == 1)
    peak_pos = np.where(peaks_pos[i] == 1)
    v = xs[int(len(xs) / 2) + peak_pos[0][0] if len(peak_pos[0]) > 0 else 0] - xs[int(len(xs) / 2) - peak_neg[0][0] if len(peak_neg[0]) > 0 else 0]
    vs.append(v)

# format
vs_neg = [vs[i] if ys[i] <= 0 else np.nan for i in range(len(ys))]
vs_pos = [vs[i] if ys[i] >= 0 else np.nan for i in range(len(ys))]

# plotter
plotter = MPLPlotter(axes={
    'X': ys,
    'Y': [0, 1]
}, params=params['plotter'])
plotter.update(xs=ys, vs=[vs_neg, vs_pos])
plotter.show(hold=True)