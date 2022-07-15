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

% power of the control laser
P_lcs = linspace(0, 10e-15, 201);

% winding number
L_ps = linspace(-10, 10, 201);

% R.-H. criterion count
Z = zeros(length(L_ps), length(P_lcs));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%                  MAIN LOOP                 %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% iterate winding numbers
for i = 1:length(L_ps)
    % first sidemode
    omega_c = hbar * (L_ps(i) + 2 * l)^2 / 2 / I;
    omega_c_tilde = omega_c + temp;
    Omega_c = sqrt((omega_c + 2 * temp)^2 - temp^2);
    % second sidemode
    omega_d = hbar * (L_ps(i) - 2 * l)^2 / 2 / I;
    omega_d_tilde = omega_d + temp;
    Omega_d = sqrt((omega_d + 2 * temp)^2 - temp^2);
    % sum and differences
    Omega_m = (Omega_c + Omega_d) / 2;
    Omega_n = (Omega_c - Omega_d);

    % detuning
    Delta_tilde = - Omega_m;

    % substituted variables
    A_mathcal = temp * (omega_c_tilde - omega_d_tilde);
    A_2 = A_mathcal^2 + Omega_c^2 * Omega_d^2;
    C = G^2 * (omega_c_tilde + omega_d_tilde) / sqrt(A_2);

    % iterate input powers
    for j = 1:length(P_lcs)
        % amplitude of the control laser
        eta_lc = sqrt(mu * gamma_o * P_lcs(j) / hbar / omega_lc);

        % coefficients of the cubic
        coeff_0 = 4 * C^2;
        coeff_1 = 8 * C * Delta_tilde;
        coeff_2 = 4 * Delta_tilde^2 + gamma_o^2;
        coeff_3 = - 4 * real(conj(eta_lc) * eta_lc);
        % roots of the cubic
        N_os = roots([coeff_0, coeff_1, coeff_2, coeff_3]);

        % stability counter
        count_stability = 0;
        % check each root
        for k = 1:length(N_os)
            % if root is real
            if imag(N_os(k)) == 0.0
                % update counter
                count_stability = count_stability + 1;

                % effective detuning
                Delta = Delta_tilde + C * real(N_os(k));

                %frequently used expressions
                D_2 = Delta^2 + gamma_o^2 / 4;
                D_N = 2 * Delta * G^2 * real(N_os(k)) * (omega_c_tilde + omega_d_tilde);
                O_2 = Omega_c^2 + Omega_d^2;

                % R.-H. coefficients
                coeffs = zeros(7);
                coeffs(1) = 1;
                coeffs(2) = 2 * gamma_m + gamma_o;
                coeffs(3) = D_2 + O_2 + gamma_m^2 + 2 * gamma_m * gamma_o;
                coeffs(4) = 2 * D_2 * gamma_m + O_2 * (gamma_m + gamma_o) + gamma_m^2 * gamma_o;
                coeffs(5) = A_2 + D_2 * (O_2 + gamma_m^2) + D_N + O_2 * gamma_m * gamma_o;
                coeffs(6) = A_2 * gamma_o + D_2 * O_2 * gamma_m + D_N * gamma_m;
                coeffs(7) = A_2 * D_2 + 2 * A_mathcal * Delta * G^2 * real(N_os(k)) * (omega_c_tilde - omega_d_tilde) + 2 * Delta * G^2 * real(N_os(k)) * (Omega_c^2 * omega_d_tilde + Omega_d^2 * omega_c_tilde);

                % matrix size
                n = 6;
                
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                % Transpiled code from the `qom` toolbox
                % https://github.com/Sampreet/qom
                % © Sampreet Kalita
                % Dt. 20220505
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                M = zeros(n, n);
                for idx_i = 1:n
                    for idx_j = 1:n
                        if (2 * (idx_i - 1) - (idx_j - 1) + 1 >= 0 && 2 * (idx_i - 1) - (idx_j - 1) + 1 <= n)
                            M(idx_i, idx_j) = coeffs(2 * idx_i - idx_j + 1);
                        end
                    end
                end
                seq = zeros(n + 1);
                seq(1) = coeffs(1);
                for idx_i = 2:n
                    sub_mat = M(1:idx_i, 1:idx_i);
                    seq(idx_i) = det(sub_mat);
                end
                flag = 0;
                for idx_i = 2:n
                    if ((seq(idx_i) / seq(idx_i - 1)) / abs(seq(idx_i) / seq(idx_i - 1)) == -1)
                        flag = 1;
                        break;
                    end
                end
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                % End of transpiled code
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

                % if not bistable but unstable
                if flag == 1
                    Z(i, j) = 1;
                end
            end
        end  
        
        % if bistable
        if count_stability > 1
            Z(i, j) = 2;
        end
    end
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%                    PLOTS                   %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% axes
[X, Y] = meshgrid(P_lcs / 1e-15, L_ps);
% colormesh
pcolor(X, Y, Z);
% x-axis properties
xlabel('$P_{lc}$ (fW)', 'Interpreter', 'latex');
% y-axis properties
ylabel('$L_{p}$', 'Interpreter', 'latex');
% cbar properties
colorbar('YTick', [0 1 2], 'YTickLabel', {'s', 'u', 'b'});