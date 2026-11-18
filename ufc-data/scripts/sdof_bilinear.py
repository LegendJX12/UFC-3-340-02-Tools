"""Maximum response of an elasto-plastic single-degree-of-freedom (SDOF) system
to a bilinear-triangular pulse, as charted in UFC 3-340-02 Figures 3-64 to 3-266.

Load (UFC 3-340-02 section 3-19.3.4, Figure 3-62): the envelope of
  shock pulse: P falling linearly to 0 at time T
  gas pulse:   C1*P falling linearly to 0 at time C2*T
i.e. p(t) = P * max(1 - t/T, C1*(1 - t/(C2*T))), zero after C2*T.
(Its impulse matches the guide's factor F, Equation 3-82.)

System: mass m, elastic stiffness k up to ultimate resistance ru, then perfectly plastic.
Nondimensional form with tau = t/Tn and u = x/XE (XE = ru/k):
  u'' = (2*pi)^2 * (P/ru * f(tau) - r(u)),  r = elastic-perfectly-plastic, |r| <= 1

Outputs (the three chart panels):
  Xm/XE    ductility ratio (maximum deflection / elastic deflection)
  tm/Tn    time of maximum deflection / natural period
  tE/T     time to reach yield / shock load duration (None if the system never yields)
"""
import math


def load_shape(tau, T, C1, C2):
    if tau >= C2 * T:
        return 0.0
    return max(1.0 - tau / T, C1 * (1.0 - tau / (C2 * T)), 0.0)


def max_response(p_over_ru, T, C1, C2, cap=1000.0):
    """T = T/Tn (load duration over natural period). Returns (Xm/XE, tm/Tn, tE/T)."""
    w2 = (2.0 * math.pi) ** 2
    t_end = C2 * T
    dt_load = min(2e-3, t_end / 2000.0)
    u = v = up = 0.0
    tau = 0.0
    tE = None

    def accel(tau, u, up):
        r = u - up
        if r > 1.0:
            r = 1.0
        elif r < -1.0:
            r = -1.0
        return w2 * (p_over_ru * load_shape(tau, T, C1, C2) - r)

    u_max, t_max = 0.0, 0.0
    falling_peaks = 0
    yielded_since_max = False
    while True:
        dt = dt_load if tau < t_end else 2e-3
        a0 = accel(tau, u, up)
        u_new = u + v * dt + 0.5 * a0 * dt * dt
        up_before = up
        if u_new - up > 1.0:          # elastic-perfectly-plastic resistance
            up = u_new - 1.0
        elif u_new - up < -1.0:
            up = u_new + 1.0
        if up != up_before:
            yielded_since_max = True
        a1 = accel(tau + dt, u_new, up)
        v_new = v + 0.5 * (a0 + a1) * dt
        if tE is None and u_new >= 1.0 and u < 1.0:
            tE = tau + dt * (1.0 - u) / (u_new - u)
        if tau > 0 and v > 0 and v_new <= 0:      # a peak
            frac = v / (v - v_new)
            t_pk = tau + frac * dt
            u_pk = u + v * frac * dt + 0.5 * a0 * (frac * dt) ** 2
            if u_pk > u_max:
                u_max, t_max = u_pk, t_pk
                falling_peaks = 0
                yielded_since_max = False
            else:
                falling_peaks += 1
            # stop once the load is over, or once peaks keep falling with no new yielding
            if t_pk >= t_end or (falling_peaks >= 2 and not yielded_since_max):
                return u_max, t_max, (tE / T if tE is not None else None)
        u, v, tau = u_new, v_new, tau + dt
        if u > cap:
            return cap, tau, (tE / T if tE is not None else None)
        if tau > 2e4:
            return max(u_max, u), t_max, (tE / T if tE is not None else None)
