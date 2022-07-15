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
% winding number
L_p         = 9;
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

% substituted variables
A_mathcal = temp * (omega_c_tilde - omega_d_tilde);
A_2 = A_mathcal^2 + Omega_c^2 * Omega_d^2;
C = G^2 * (omega_c_tilde + omega_d_tilde) / sqrt(A_2);

% critical detuning 
Delta_tilde_cr = - sqrt(3) * gamma_o / 2;
% frequency of the control laser
omega_lc = 2 * pi * c / lambda_lc;
% critical power of the control laser;
P_cr = gamma_o^2 * hbar * omega_lc / 3 / sqrt(3) / C / mu;

% power of the control laser
P_lcs = linspace(0, 5e-15, 1001);

% laser detuning normalized by critical values
Delta_tildes = [0.5, 1.0, 1.5] * Delta_tilde_cr;

% power corresponding to multiple values of occupancy
P_lc_multis = zeros(length(Delta_tildes), length(P_lcs));
% multiple values of mean optical occupancy
N_o_multis = zeros(length(Delta_tildes), length(P_lcs));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%                  MAIN LOOP                 %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% iterate detunings
for i = 1:length(Delta_tildes)
    % counter 
    idx = 1;

    % iterate input powers
    for j = 1:length(P_lcs)
        % amplitude of the control laser
        eta_lc = sqrt(mu * gamma_o * P_lcs(j) / hbar / omega_lc);

        % coefficients of the cubic
        coeff_0 = 4 * C^2;
        coeff_1 = 8 * C * Delta_tildes(i);
        coeff_2 = 4 * Delta_tildes(i)^2 + gamma_o^2;
        coeff_3 = - 4 * real(conj(eta_lc) * eta_lc);
        % roots of the cubic
        N_os = roots([coeff_0, coeff_1, coeff_2, coeff_3]);
        % check each root
        for k = 1:length(N_os)
            % if root is real
            if imag(N_os(k)) == 0.0
                % update lists
                P_lc_multis(i, idx) = P_lcs(j);
                N_o_multis(i, idx) = real(N_os(k));
                idx = idx + 1;
            end
        end  
    end
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%                    PLOTS                   %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% plot
hold on
scatter(P_lc_multis(1, :) / 1e-15, N_o_multis(1, :), 1, 'b', 'filled')
scatter(P_lc_multis(2, :) / 1e-15, N_o_multis(2, :), 1, 'g', 'filled')
scatter(P_lc_multis(3, :) / 1e-15, N_o_multis(3, :), 1, 'r', 'filled')
hold off
% x-axis properties
xlabel('$P_{lc}$ (fW)', 'Interpreter', 'latex')
% y-axis properties
ylabel('$N_{o}$', 'Interpreter', 'latex')
% legend
legend('$\tilde{\Delta} = 0.5 \tilde{\Delta}_{cr}$', '$\tilde{\Delta} = \tilde{\Delta}_{cr}$', '$\tilde{\Delta} = 1.5 \tilde{\Delta}_{cr}$', 'Interpreter', 'latex')