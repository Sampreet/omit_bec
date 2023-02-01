# dependencies
import numpy as np
import os 
import sys

# qom modules
from qom.utils.looper import run_loopers_in_parallel

# add path to local libraries
sys.path.append(os.path.abspath(os.path.join('..', 'bec-systems')))
# import system
from systems import BEC_10

# all parameters
params = {
    'looper': {
        'X': {
            'var': 'P_lc',
            'min': 0.0,
            'max': 10e-15,
            'dim': 1001,
            'scale': 'linear'
        },
        'Y': {
            'var': 'L_p',
            'min': 0,
            'max': 10,
            'dim': 101,
            'scale': 'linear'
        }
    },
    'system': {
        'Delta_tilde'   : -1.0,
        'delta'         : 0.0,
        'G'             : 2 * np.pi * 1e3,
        'g_tilde_norm'  : 0.0,
        'gamma_m'       : 2 * np.pi * 0.8,
        'gamma_o'       : 2 * np.pi * 1e3,
        'k'             : 1,
        'L_p'           : 1,
        'l'             : 20,
        'lambda_lc'     : 589e-9,
        'm'             : 23,
        'mu'            : 0.5,
        'N'             : 1e4,
        'P_lc'          : 1e-15,
        'P_lp_norm'     : 0.01,
        'R'             : 10e-6,
        't_approx'      : 'none',
        't_Delta_norm'  : 'Omega_m',
        't_Delta_offset': 'zero',
        't_delta_norm'  : 'Omega_m',
        't_delta_offset': 'Omega_m',
        't_line'        : 's',
        't_oss_method'  : 'cubic',
        't_P_lc_norm'   : 'none'
    },
    'plotter': {
        'type': 'pcolormesh',
        'palette': 'RdBu_r',
        'x_label': '$P_{lc}$ (fW)',
        'x_tick_labels': [i * 2 for i in range(6)],
        'x_tick_pad': 16,
        'x_ticks': [i * 2e-15 for i in range(6)],
        'x_ticks_minor': [i * 0.5e-15 for i in range(21)],
        'y_label': '$L_{p}$',
        'y_tick_pad': 16,
        'y_ticks': [i * 2 for i in range(6)],
        'y_ticks_minor': [i * 0.5 for i in range(21)],
        'v_ticks': [0, 1, 2, 3],
        'annotations': [{
            's': '(b)',
            'xy': (0.185, 0.86)
        }, {
            's': 's',
            'xy': (0.4, 0.55),
            'color': 'k',
            'font_dict': 'tick'
        }, {
            's': 'u',
            'xy': (0.8, 0.55),
            'color': 'w',
            'font_dict': 'tick'
        }],
        'label_font_size': 40.0,
        'tick_font_size': 32.0,
        'height': 8.0,
        'width': 9.6
    }
}

# looper
if __name__ == '__main__':
    run_loopers_in_parallel(SystemClass=BEC_10, params=params, func='osz', looper='XYLooper', file_path_prefix='data/v3.5-qom-v0.9.0/2b', plot=True,)