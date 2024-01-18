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
        'file_path_prefix'  : 'data/v3.5_qom-v1.0.1/7',
        'X'                 : {
            'var'   : 'delta',
            'min'   : -0.5,
            'max'   : 0.5,
            'dim'   : 10001
        },
        'Y'                 : {
            'var'   : 'Delta_tilde',
            'val'   : [-0.8, -0.9, -1.0, -1.1, -1.2]
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
        't_oss_method'  : 'basic',
        't_P_lc_norm'   : 'none'
    },
    'plotter': {
        'type'              : 'lines_3d',
        'colors'            : ['b', 'k', 'r', 'g', 'm'],
        'sizes'             : [2] * 5,
        'styles'            : ['-', ':', '--', '-.', ':'],
        'x_label_pad'       : 32,
        'x_label'           : '$\\left( \\delta - \\Omega_{m} \\right) / \\Omega_{m}$',
        'x_tick_pad'        : 0,
        'x_ticks'           : [-0.5, 0.0, 0.5],
        'x_ticks_minor'     : [i * 0.25 - 0.5 for i in range(5)],
        'y_label_pad'       : 48,
        'y_label'           : '$\\tilde{\\Delta} / \\Omega_{m}$',
        'y_limits'          : [-1.22, -0.78],
        'y_tick_labels'     : [-1.2, -1.1, -1.0, -0.9, -0.8],
        'y_tick_pad'        : 4,
        'y_ticks'           : [i * 0.1 - 1.2 for i in range(5)],
        'y_ticks_minor'     : [i * 0.1 - 1.2 for i in range(5)],
        'v_label_pad'       : 20,
        'v_label'           : '$T$',
        'v_tick_pad'        : 8,
        'v_ticks'           : [0.0, 0.5, 1.0],
        'v_ticks_minor'     : [i * 0.1 for i in range(11)],
        'label_font_size'   : 32.0,
        'tick_font_size'    : 26.0,
        'width'             : 9.6,
        'height'            : 8.0,
        'view_aspect'       : [1.0, 1.5, 0.75],
        'view_elevation'    : 28,
        'view_rotation'     : -45
    }
}

# function to obtain the transmission
def func_transmission(system_params):
    # intialize system
    system = BEC_10(
        params=system_params
    )
    _, _, c = system.get_ivc()
    # return transmission
    return system.get_transmission(
        c=c
    )

# looper
looper = wrap_looper(
    looper_name='XYLooper',
    func=func_transmission,
    params=params['looper'],
    params_system=params['system'],
    plot=True,
    params_plotter=params['plotter']
)