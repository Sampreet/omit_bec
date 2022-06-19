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
            'min': -10e3,
            'max': 10e3,
            'dim': 20001
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
        'x_label': '$d \\delta$\n(KHz)',
        'x_label_pad': -14,
        'x_tick_labels': [0, '', 20],
        'x_ticks': [i * 10e3 for i in range(3)],
        'x_ticks_minor': [i * 5e3 for i in range(5)],
        'v_label': '$L_{p}$',
        'v_label_pad': -24,
        'v_limits': [-10, 10],
        'v_tick_labels': [-9, '', 9],
        'v_ticks': [i * 9 - 9 for i in range(3)],
        'v_ticks_minor': [i * 3 - 9 for i in range(7)],
        'height': 2.5,
        'width': 1.5,
        'annotations': [{
            's': '(f)',
            'xy': (0.07, 0.085)
        }]
    }
}

# looper
looper = wrap_looper(SystemClass=BEC_00, params=params, func='transmission', looper='XYLooper', file_path_prefix='data/bec_00/v0.13/2f')

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

# plotter
plotter = MPLPlotter(axes={
    'X': vs
}, params=params['plotter'])
plotter.update(xs=vs, vs=ys)
plotter.show(hold=True)