# dependencies
import numpy as np
import os 
import sys

# qom modules
from qom.ui.plotters import MPLPlotter
from qom.utils.looper import run_loopers_in_parallel

# add path to local libraries
sys.path.append(os.path.abspath(os.path.join('..', 'bec-systems')))
# import system
from systems import BEC_10

# all parameters
params = {
    'looper': {
        'X': {
            'var': 'delta',
            'min': -4.0,
            'max': 4.0,
            'dim': 800001
        },
        'Y': {
            'var': 'L_p',
            'min': 0,
            'max': 10,
            'dim': 11
        },
        'Z': {
            'var': 'l',
            'val': [18, 20, 22, 24]
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
        'P_lc'          : 0.5e-15,
        'P_lp_norm'     : 0.01,
        'R'             : 10e-6,
        't_approx'      : 'none',
        't_Delta_norm'  : 'Omega_m',
        't_Delta_offset': 'zero',
        't_delta_norm'  : 'gamma_o',
        't_delta_offset': 'Omega_m',
        't_line'        : 's',
        't_oss_method'  : 'basic',
        't_P_lc_norm'   : 'none'
    },
    'plotter': {
        'type': 'lines',
        'x_label': '$L_{p}$',
        'x_ticks': [i * 2 for i in range(6)],
        'x_ticks_minor': [i * 0.5 for i in range(21)],
        'y_colors': ['k', 'r', 'g', 'b'],
        'y_name': '$l$',
        'y_sizes': [2] * 4,
        'v_label': '$d \\delta / \\gamma_{o}$',
        'v_ticks': [i for i in range(6)],
        'v_ticks_minor': [i * 0.25 for i in range(21)],
        'show_legend': True,
        'legend_location': 'upper center',
        'legend_font_size': 32.0,
        'label_font_size': 40.0,
        'tick_font_size': 32.0,
        'height': 8.0,
        'width': 9.6
    }
}

# function to calculate transmission
def func_transmission(system_params, val, logger, results):
    # initialize system
    system = BEC_10(params=system_params)
    # extract parameters
    _, c = system.get_ivc()
    _, params = system._get_D_params_ivp(c)
    # get transmission
    T = system.get_transmission(params=params)
    # update results
    results.append((val, T))

if __name__ == '__main__':
    # looper
    looper = run_loopers_in_parallel(SystemClass=BEC_10, params=params, func=func_transmission, looper='XYZLooper', file_path_prefix='data/v3.5-qom-v0.9.0/6')
    delta_norms = looper.axes['X']['val']
    xs = looper.axes['Y']['val']
    ys = looper.axes['Z']['val']
    vs = looper.results['V']

    # calculate peak differences
    ddelta_norms = list()
    for i in range(len(vs)):
        ddelta_norms_temp = list()
        for j in range(len(vs[0])):
            # for each transparency profile
            Ts = vs[i][j]
            dim = len(Ts)
            k = int(dim / 2) + 1 if dim % 2 == 0 else int(dim / 2)
            # locate change of derivative from positive to negative from center
            idxs = list()
            while k <= dim - 2 and len(idxs) < 2:
                if Ts[k] - Ts[k - 1] >= 0 and Ts[k + 1] - Ts[k] <= 0:
                    idxs.append(k)
                if Ts[- k - 1] - Ts[- k] >= 0 and Ts[- k - 2] - Ts[- k - 1] <= 0:
                    idxs.append(- k - 1)
                k += 1
            # update list with difference between peaks
            ddelta_norms_temp.append(np.abs(delta_norms[idxs[-1]] - delta_norms[idxs[0]]))
        # update main list
        ddelta_norms.append(ddelta_norms_temp)

    # plotter
    plotter = MPLPlotter(axes={
        'X': xs,
        'Y': ys
    }, params=params['plotter'])
    plotter.update(xs=xs, vs=ddelta_norms)
    plotter.show(hold=True)