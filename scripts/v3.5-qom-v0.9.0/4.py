# dependencies
import numpy as np
import os 
import sys

# qom modules
from qom.ui.plotters import MPLPlotter
from qom.utils.looper import run_loopers_in_parallel, wrap_looper

# add path to local libraries
sys.path.append(os.path.abspath(os.path.join('..', 'bec-systems')))
# import system
from systems import BEC_10

# all parameters
params = {
    'looper': {
        'X': {
            'var': 'delta',
            'min': -0.2,
            'max': 0.2,
            'dim': 400001
        },
        'Y': {
            'var': 'P_lc',
            'min': 0.0e-15,
            'max': 1.5e-15,
            'dim': 151
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
        'x_label': '$P_{lc}$ (fW)',
        'x_tick_labels': [0.0, 0.3, 0.6, 0.9, 1.2, 1.5],
        'x_ticks': [i * 0.3e-15 for i in range(6)],
        'x_ticks_minor': [i * 0.1e-15 for i in range(16)],
        'y_colors': ['b', 'g', 'r', 'm'],
        'y_sizes': [2] * 4,
        'y_styles': ['-', '--'] * 2,
        'v_label': '$T ~ |_{\\delta = \\Omega_{m}}$',
        'v_label_color': 'b',
        'v_tick_labels': ['{:0.1f}'.format(i * 0.2) for i in range(6)],
        'v_ticks': [i * 0.2 for i in range(6)],
        'v_ticks_minor': [i * 0.1 for i in range(11)],
        'v_twin_label': '$\\Gamma_{m} / \\Omega_{m}$',
        'v_twin_label_color': 'r',
        'v_twin_tick_labels': ['{:0.2f}'.format(i * 0.01) for i in range(6)],
        'v_twin_ticks': [i * 0.01 for i in range(6)],
        'v_twin_ticks_minor': [i * 0.005 for i in range(11)],
        'label_font_size': 32.0,
        'tick_font_size': 26.0,
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
    # get transparency
    T = system.get_transmission(params=params)
    # update results
    results.append((val, T))

if __name__ == '__main__':
    # get transmission values
    looper = run_loopers_in_parallel(SystemClass=BEC_10, params=params, func=func_transmission, looper='XYLooper', file_path_prefix='data/v3.5-qom-v0.9.0/4_' + params['system']['t_approx'] + '_' + params['system']['t_oss_method'], plot=False)

    # extract axes
    xs = looper.axes['X']['val']
    ys = looper.axes['Y']['val']
    vs = looper.results['V']
    # calculate maximum transmission
    Ts_maxi = [0]
    for i in range(1, len(vs)):
        Ts = vs[i]
        dim = len(Ts)
        k = int(dim / 2) + 1 if dim % 2 == 0 else int(dim / 2)
        # locate change of derivative from positive to negative from center
        while k <= dim - 2:
            if Ts[k] - Ts[k - 1] >= 0 and Ts[k + 1] - Ts[k] <= 0:
                Ts_maxi.append(Ts[k])
                break
            if Ts[- k - 1] - Ts[- k] >= 0 and Ts[- k - 2] - Ts[- k - 1] <= 0:
                Ts_maxi.append(Ts[- k - 1])
                break
            k += 1

    # calculate transmission at resonance
    Ts_reso = [v[int(len(v) / 2)] for v in vs]

    # calculate normailzed FWHM
    Gamma_ms_reso = [0]
    for i in range(1, len(vs)):
        Ts = vs[i]
        dim = len(Ts)
        mid = int(dim / 2) + 1 if dim % 2 == 0 else int(dim / 2)
        k = mid
        # locate half maxima
        idxs = list()
        flags = [0, 0]
        while k <= dim - 2 and len(idxs) < 2:
            if Ts[k] <= Ts_reso[i] / 2 and flags[1] == 0:
                idxs.append(k)
                flags[1] = 1
            if Ts[- k - 1] <= Ts_reso[i] / 2 and flags[0] == 0:
                idxs.append(- k - 1)
                flags[0] = 1
            k += 1
        Gamma_ms_reso.append(np.abs(xs[idxs[-1]] - xs[idxs[0]]))

    # get transmission at resonance
    looper_Ts_reso = wrap_looper(SystemClass=BEC_10, params={
            'looper': {
                'X': params['looper']['Y']
            },
            'system': params['system']
        }, func='transmission_resonance', looper='XLooper', plot=False)
    Ts_reso_expr = looper_Ts_reso.results['V']

    # get normalized FWHM
    looper_Gamma_ms_reso = wrap_looper(SystemClass=BEC_10, params={
            'looper': {
                'X': params['looper']['Y']
            },
            'system': params['system']
        }, func='fwhm_norm_resonance', looper='XLooper', plot=False)
    Gamma_ms_reso_expr = looper_Gamma_ms_reso.results['V']

    # plotter
    plotter = MPLPlotter(axes={
        'X': ys
    }, params=params['plotter'])
    plotter.update(xs=ys, vs=[Ts_maxi, Ts_reso_expr])
    plotter.update_twin_axis(xs=ys, vs=[Gamma_ms_reso, Gamma_ms_reso_expr])
    plotter.show(True)