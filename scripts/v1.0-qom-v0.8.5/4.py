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
            'min': -20e3,
            'max': 20e3,
            'dim': 40001
        },
        'Y': {
            'var': 'L_p',
            'min': -12,
            'max': 12,
            'dim': 121,
            'scale': 'linear'
        }
    },
    'system': {
        'G': 2 * np.pi * 1e3,
        't_detuning': 'Omega_m',
        't_offset': 'Omega_m'
    },
    'plotter': {
        'type': 'lines',
        'x_label': '$L_{p}$',
        'x_ticks': [i * 6 - 12 for i in range(5)],
        'x_ticks_minor': [i * 2 - 12 for i in range(13)],
        'y_colors': ['b', 'b'],
        'y_styles': ['--', '-'],
        'v_label': '$d \\delta$ (KHz)',
        'v_tick_labels': [i * 8 for i in range(4)],
        'v_ticks': [i * 8e3 for i in range(4)],
        'v_ticks_minor': [i * 4e3 for i in range(7)],
        'height': 3.0,
        'width': 4.8
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission', looper='XYLooper', file_path_prefix='data/v1.0-qom-v0.8.5/4')

# frequently used variables
xs = looper.axes['X']['val']
ys = looper.axes['Y']['val']
V = looper.results['V']

# get peaks
peaks = [np.where(np.array(V[i]) > 0.95, 1, 0) for i in range(len(V))]
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