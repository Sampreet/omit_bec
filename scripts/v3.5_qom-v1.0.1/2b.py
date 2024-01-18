# dependencies
import numpy as np
import os 
import sys

# qom modules
from qom.utils.solvers import get_func_stability_zone
from qom.utils.loopers import run_loopers_in_parallel, wrap_looper

# add path to local libraries
sys.path.append(os.path.abspath(os.path.join('.')))
# import system
from systems.BoseEinsteinCondensate import BEC_10

# all parameters
params = {
    'looper': {
        'show_progress'     : True,
        'file_path_prefix'  : 'data/v3.5_qom-v1.0.1/2b',
        'X'                 : {
            'var'   : 'P_lc',
            'min'   : 0.0,
            'max'   : 10e-15,
            'dim'   : 1001,
            'scale' : 'linear'
        },
        'Y'                 : {
            'var'   : 'L_p',
            'min'   : 0,
            'max'   : 10,
            'dim'   : 101,
            'scale' : 'linear'
        }
    },
    'solver': {
        'show_progress'         : False,
        'use_system_method'     : True,
        'system_measure_name'   : 'coeffs_A'
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
        'type'              : 'pcolormesh',
        'palette'           : 'copper_r',
        'x_label'           : '$P_{lc}$ (fW)',
        'x_tick_labels'     : [i * 2 for i in range(6)],
        'x_tick_pad'        : 16,
        'x_ticks'           : [i * 2e-15 for i in range(6)],
        'x_ticks_minor'     : [i * 0.5e-15 for i in range(21)],
        'y_label'           : '$L_{p}$',
        'y_tick_pad'        : 16,
        'y_ticks'           : [i * 2 for i in range(6)],
        'y_ticks_minor'     : [i * 0.5 for i in range(21)],
        'v_ticks'           : [5, 9],
        'label_font_size'   : 40.0,
        'tick_font_size'    : 32.0,
        'width'             : 9.6,
        'height'            : 8.0,
        'annotations'       : [{
            'text'      : '(b)',
            'xy'        : (0.185, 0.86)
        }, {
            'text'      : 's',
            'xy'        : (0.4, 0.55),
            'color'     : 'k',
            'font_dict' : 'tick'
        }, {
            'text'      : 'u',
            'xy'        : (0.8, 0.55),
            'color'     : 'w',
            'font_dict' : 'tick'
        }],
    }
}

# function to obtain the stability zone
def func_stability_zone(system_params):
    # return function
    return get_func_stability_zone(
        SystemClass=BEC_10,
        params=params['solver'],
        steady_state=True,
        use_rhc=False
    )(
        system_params=system_params
    )

# looper
if __name__ == '__main__':
    looper = run_loopers_in_parallel(
        looper_name='XYLooper',
        func=func_stability_zone,
        params=params['looper'],
        params_system=params['system'],
        plot=True,
        params_plotter=params['plotter']
    )