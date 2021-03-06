import numpy as np
from scipy.optimize import linprog
import random
import generate_rt_prices
# price = np.zeros(4)
#
# for i in range(len(price)):
#     price[i] = random.uniform(0.1, 0.5)

h = 24

np.random.seed(4)
pr = np.random.random(h)
print(pr)
c = np.append(pr, pr)

A_ineq = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

b_ineq = np.array([3, 3, 3, 3, 3, 1.5, 1.5, 1.5, 1.5, 1.5])

A_eq = np.array([[1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]])

res = linprog(c, A_ub=A_ineq, b_ub=b_ineq, A_eq=A_eq, b_eq=b_eq)
print(res)


