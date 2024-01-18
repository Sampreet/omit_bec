# dependencies
import numpy as np
import os 
import sys

# qom modules
from qom.utils.loopers import wrap_looper

# add path to local libraries
sys.path.append(os.path.abspath(os.path.join('.')))
# import system
from systems.BoseEinsteinCondensate import BEC_10

# all parameters
params = {
    'looper': {
        'show_progress'     : True,
        'file_path_prefix'  : 'data/v3.5_qom-v1.0.1/2a',
        'X'                 : {
            'var'   : 'P_lc',
            'min'   : 0.0,
            'max'   : 90e-15,
            'dim'   : 9001,
            'scale' : 'linear'
        },
        'Y'                 : {
            'var'   : 'g_tilde_norm',
            'val'   : [0.0, 12.0]
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
        'L_p'           : 0,
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
        'type'              : 'scatters',
        'colors'            : ['b', 'k'],
        'sizes'             : [10, 50],
        'styles'            : ['s', '.'],
        'x_label'           : '$P_{lc}$ (fW)',
        'x_tick_labels'     : [i * 15 for i in range(7)],
        'x_tick_pad'        : 16,
        'x_ticks'           : [i * 15e-15 for i in range(7)],
        'x_ticks_minor'     : [i * 5e-15 for i in range(19)],
        'v_label'           : '$\\left| \\alpha_{s} \\right|^{2}$',
        'v_tick_pad'        : 16,
        'v_ticks'           : [i * 2 for i in range(6)],
        'v_ticks_minor'     : [i * 0.5 for i in range(21)],
        'show_legend'       : True,
        'legend_labels'     : ['$\\tilde{g} = 0$', '$\\tilde{g} = 12 \\tilde{g}_{m}$', '$\\tilde{g} = 40 \\tilde{g}_{m}$'],
        'legend_location'   : 'center right',
        'label_font_size'   : 40.0,
        'legend_font_size'  : 32.0,
        'tick_font_size'    : 32.0,
        'width'             : 9.6,
        'height'            : 8.0,
        'annotations'       : [{
            'text'  : '(a)',
            'xy'    : (0.19, 0.86)
        }]
    }
}

# function to obtain the mean optical occupancies
def func_moo(system_params):
    # intialize system
    system = BEC_10(
        params=system_params
    )
    # get mean optical occupancies
    N_os = system.get_mean_optical_occupancies()

    return N_os

# looper
looper = wrap_looper(
    looper_name='XYLooper',
    func=func_moo,
    params=params['looper'],
    params_system=params['system'],
    plot=True,
    params_plotter=params['plotter']
)