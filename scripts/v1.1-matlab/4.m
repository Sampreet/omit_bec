%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%               INITIALIZATION               %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% clear
clc;
close all;
clear all;

% exact constants from Python
amu = 1.6605390666e-27;
c = 299792458.0;
hbar = 1.0545718176461565e-34;
pi = 3.141592653589793;

% % approximate constants used for PRL.127.113601
% amu = 1.6e-27;
% c = 3e8;
% hbar = 1.05e-34;
% pi = 3.1416;

% optomechanical coupling strength
G           = 2 * pi * 1e3;
% normalized atom-atom interaction strength
g_tilde_norm= 0.0;
% mechanical damping rate
gamma_m     = 2 * pi * 0.8;
% optical decay rate
gamma_o     = 2 * pi * 1e3;
% OAM number
l           = 25;
% frequency of control laser
lambda_lc   = 589e-9;
% mass of Sodium atom
m           = 23;
% laser-cavity coupling parameter
mu          = 0.5;
% number of Sodium atoms
N           = 1e4;
% radius of the ring-BEC
R           = 12e-6;

% moment of inertia
I = m * amu * R^2;

% atomic interactions
g_tilde = g_tilde_norm * hbar / 4 / I / N;

% frequency of the control laser
omega_lc = 2 * pi * c / lambda_lc;

% frequently used variable
temp = 2 * g_tilde * N;

% detuning frequency with reference to a fixed offset
delta_offsets = linspace(-2, 2, 40001) * gamma_o;

% winding numbers
L_ps = -10:0.1:10;

% transmission values
Ts = zeros(length(L_ps), length(delta_offsets));
% peak position differences
peak_diffs = zeros(length(L_ps));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%                  MAIN LOOP                 %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% iterate winding numbers
for i = 1:length(L_ps)
    % winding number
    L_p = L_ps(i)
    % first sidemode
    omega_c = hbar * (L_p + 2 * l)^2 / 2 / I;
    omega_c_tilde = omega_c + temp;
    Omega_c = sqrt((omega_c + 2 * temp)^2 - temp^2);
    % second sidemode
    omega_d = hbar * (L_p - 2 * l)^2 / 2 / I;
    omega_d_tilde = omega_d + temp;
    Omega_d = sqrt((omega_d + 2 * temp)^2 - temp^2);
    % sum and differences
    Omega_m = (Omega_c + Omega_d) / 2;
    Omega_n = (Omega_c - Omega_d);

    % create lists for comprehension
    omega_tildes = [omega_c_tilde, omega_d_tilde];
    Omegas = [Omega_c, Omega_d];

    % substituted variables
    A_mathcal = temp * (omega_c_tilde - omega_d_tilde);
    A_2 = A_mathcal^2 + Omega_c^2 * Omega_d^2;
    C = G^2 * (omega_c_tilde + omega_d_tilde) / sqrt(A_2);

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % absolute power of the control laser
    P_lc = 2e-15;
    % amplitude of the control laser
    eta_lc = sqrt(mu * gamma_o * P_lc / hbar / omega_lc);
    % detuning of the control laser
    Delta_tilde = - Omega_m;
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    % coefficients of the cubic
    coeff_0 = 4 * C^2;
    coeff_1 = 8 * C * Delta_tilde;
    coeff_2 = 4 * Delta_tilde^2 + gamma_o^2;
    coeff_3 = - 4 * real(conj(eta_lc) * eta_lc);
    % roots of the cubic
    N_os = roots([coeff_0, coeff_1, coeff_2, coeff_3]);
    % check each root
    N_o = 0;
    for j = 1:length(N_os)
        % if root is real
        if imag(N_os(j)) == 0.0
            % select root
            N_o = real(N_os(j));
            break
        end
    end
    % effective detuning
    Delta = Delta_tilde + C * N_o;

    % iterate offset probe detunings
    for j = 1:length(delta_offsets)
        % offset probe detuning
        delta_offset = delta_offsets(j);

        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        % offset for probe detuning
        offset = Omega_m;
        % probe detuning
        delta = delta_offset + offset;
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        % effective decay rates
        Gamma_m = gamma_o / 2 - 1j * (Delta + delta);
        Gamma_p = gamma_o / 2 + 1j * (Delta - delta);

        % effective susceptibilities
        chis =  [1 / (Omegas(1)^2 - 1j * delta * gamma_m - delta^2), 1 / (Omegas(2)^2 - 1j * delta * gamma_m - delta^2)];

        % numerator of Lambda
        num = A_mathcal * chis(1) * chis(2) * (omega_c - omega_d);
        num = num + chis(1) * omega_tildes(1) + chis(2) * omega_tildes(2);
        % denominator of Lambda
        den = A_mathcal^2 * chis(1) * chis(2) + 1;
        % Lambda
        Lambda = num / den;

        % transmission coefficeint without any approximation
        num_s = mu * gamma_o * (Gamma_p + 1j * G^2 * Lambda * N_o);
        den = Gamma_m * Gamma_p + 2 * Delta * G^2 * Lambda * N_o;
        t_s = 1 - num_s / den;

        % transmission
        T = real(conj(t_s) * (t_s));

        % update temporary lists
        Ts(i, j) = T;
    end

    % calculate gradients
    grads = gradient(Ts(i, :));
    % locate peak position on positive side
    for j=round(length(delta_offsets) / 2) - 1:1:length(delta_offsets)
        % if gradient changes sign from positive to negative
        if grads(j) < 0.0 && Ts(i, j) > 0.9
            peak_pos = delta_offsets(j);
            break
        end
    end
    % locate peak position on negative side
    for j=round(length(delta_offsets) / 2) - 1:-1:1
        % if gradient changes sign from negative to positive
        if grads(j) > 0.0 && Ts(i, j) > 0.9
            peak_neg = delta_offsets(j);
            break
        end
    end

    % update peak differences
    peak_diffs(i) = peak_pos - peak_neg;
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%                    PLOTS                   %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% plot
hold on
plot(L_ps(1:round(length(L_ps) / 2)), peak_diffs(1:round(length(L_ps) / 2)) / gamma_o, '--b')
plot(L_ps(round(length(L_ps) / 2):length(L_ps)), peak_diffs(round(length(L_ps) / 2):length(L_ps)) / gamma_o, '-b')
hold off
% x-axis properties
xlabel('$L_{p}$', 'Interpreter', 'latex')
xlim([-10, 10])
% y-axis properties
ylabel('$d \delta / \gamma_{o}$', 'Interpreter', 'latex')
ylim([0, 3])