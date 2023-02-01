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
        'grad': True,
        'X': {
            'var': 'delta',
            'min': -0.002,
            'max': 0.002,
            'dim': 400001
        },
        'Y': {
            'var': 'L_p',
            'min': 0,
            'max': 10,
            'dim': 101
        },
        'Z': {
            'var': 'P_lc',
            'val': [0.5e-15, 1e-15, 1.5e-15, 2e-15]
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
        't_approx'      : 'res',
        't_Delta_norm'  : 'Omega_m',
        't_Delta_offset': 'zero',
        't_delta_norm'  : 'Omega_m',
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
        'y_name': '$P_{lc}$',
        'y_unit': 'fW',
        'y_sizes': [2] * 4,
        'v_label': '$\\tau_{g}$ (s)',
        'v_ticks': [-i * 50 for i in range(4)],
        'v_ticks_minor': [-i * 10 for i in range(16)],
        'show_legend': True,
        'legend_location': 'center left',
        'annotations': [{
            's': '(b)',
            'xy': (0.86, 0.86)
        }],
        'legend_font_size': 32.0,
        'label_font_size': 40.0,
        'tick_font_size': 32.0,
        'height': 8.0,
        'width': 9.6
    }
}

# function to calculate normalized transmission phase
def func_transmission_phase_norm(system_params, val, logger, results):
    # initialize system
    system = BEC_10(params=system_params)
    # extract parameters
    _, c = system.get_ivc()
    _, params = system._get_D_params_ivp(c)
    # get transmission phase
    phi = system.get_transmission_phase(params=params)
    # normalize by additive detuning
    _, Omegas, _, _ = system.get_effective_values(params=params)
    phi_norm = phi / (Omegas[0] + Omegas[1]) * 2
    # update results
    results.append((val, phi_norm))

if __name__ == '__main__':
    # looper
    looper = run_loopers_in_parallel(SystemClass=BEC_10, params=params, func=func_transmission_phase_norm, looper='XYZLooper', file_path_prefix='data/v3.5-qom-v0.9.0/10b')
    xs = looper.axes['Y']['val']
    vs = [[np.min(col) for col in row] for row in looper.results['V']]

    # plotter
    plotter = MPLPlotter(axes={
        'X': xs,
        'Y': [0.5, 1.0, 1.5, 2.0]
    }, params=params['plotter'])
    plotter.update(xs=xs, vs=vs)
    plotter.show(hold=True)