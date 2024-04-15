import math

from scipy.optimize import linprog


class BreakLoop(Exception):
    pass


l_min = 4.8
l_max = 12.8
L_min = 9.0
L_max = 10.0
L_best = 9.5

for L in (62.7, 66):
    min_lost = math.inf
    min_m = min_n = min_p = 0
    min_x = None

    m_max = math.floor(L / L_min)
    for m in range(0, m_max + 1):
        n_max = math.floor((L - m * L_min) / L_max)
        for n in range(0, n_max + 1):
            p_max = math.floor((L - m * L_min - n * L_max) / l_min)
            for p in range(0, p_max + 1):
                if m + n + p == 0:
                    continue
                c = [0] * m + [1] * n + [1] * p
                A_eq = [[1] * m + [1] * n + [1] * p]
                b_eq = [L]
                bounds = [(L_min, L_max)] * m + [(L_max, l_max)] * n + [(l_min, L_min)] * p
                res = linprog(c=c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
                if res.success:
                    lost = res.fun - n * L_max
                    if lost < min_lost:
                        min_lost = lost
                        min_m = m
                        min_n = n
                        min_p = p
                        min_x = res.x

    m_best_max = math.floor(L / L_best)
    try:
        m_max = math.floor(L / L_min)
        for m_best in range(m_best_max, -1, -1):
            for m in range(0, m_max + 1):
                n_max = math.floor((L - m * L_min) / L_max)
                for n in range(0, n_max + 1):
                    p_max = math.floor((L - m * L_min - n * L_max) / l_min)
                    for p in range(0, p_max + 1):
                        if m + n + p == 0:
                            continue
                        c = [0] * m + [0] * n + [0] * p
                        A_eq = [
                            [1] * m + [1] * n + [1] * p,
                            [0] * m + [1] * n + [1] * p,
                        ]
                        b_eq = [round(L - m_best * L_best, 1), round(min_lost, 1) + n * L_max]
                        bounds = [(L_min, L_max)] * m + [(L_max, l_max)] * n + [(l_min, L_min)] * p
                        res = linprog(c=c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
                        if res.success:
                            raise BreakLoop
    except BreakLoop:
        pass

    x = [L_best] * m_best + list(res.x)
    print(f"Optimal solution for L = {L} is {x} with lost {min_lost}, m_best = {m_best}")

# Output:
# Optimal solution for L = 62.7 is [12.700000000000003, 10.0, 10.0, 10.0, 10.0, 10.0] with lost 2.700000000000003, m_best = 0
# Optimal solution for L = 66 is [9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.0] with lost 0.0, m_best = 6
