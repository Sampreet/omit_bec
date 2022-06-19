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
        'x_label': '$d \\delta$ (KHz)',
        'x_label_pad': -14,
        'x_tick_labels': [0, 5, '', 15, 20],
        'x_ticks': [i * 5e3 for i in range(5)],
        'x_ticks_minor': [i * 2.5e3 for i in range(9)],
        'y_colors': ['b', 'b'],
        'y_styles': ['-', '--'],
        'v_label': '$L_{p}$',
        'v_label_pad': -24,
        'v_tick_labels': [-12, '', 12],
        'v_ticks': [i * 12 - 12 for i in range(3)],
        'v_ticks_minor': [i * 6 - 12 for i in range(5)],
        'height': 2.0,
        'width': 4.8,
        'annotations': [{
            's': '(a)',
            'xy': (0.125, 0.76)
        }]
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission', looper='XYLooper', file_path_prefix='data/bec_00/v0.14/5a')

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
ys_neg = [y if y <= 0 else np.nan for y in ys]
ys_pos = [y if y >= 0 else np.nan for y in ys]

# plotter
plotter = MPLPlotter(axes={
    'X': vs,
    'Y': [0, 1]
}, params=params['plotter'])
plotter.update(xs=vs, vs=[ys_pos, ys_neg])
plotter.show(hold=True)