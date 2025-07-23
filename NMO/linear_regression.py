import numpy as np
import matplotlib.pyplot as plt
from gauss_elimination import rref, back_subs


if __name__ == '__main__':
    x = np.array(input("Enter the x values: ").split(), dtype=np.float32)
    y = np.array(input("Enter the y values: ").split(), dtype=np.float32)
    sum_x = x.sum()
    n = len(x)
    sum_x_2 = (x**2).sum()
    sum_y = y.sum()
    sum_xy = (x*y).sum()

    coeffs = np.array([[sum_x, n],
                    [sum_x_2, sum_x]])

    sol_mat = np.array([sum_y, sum_xy]).reshape(-1, 1)
    # coeffs, sol_mat
    coeffs, sol_mat = rref(coeffs, sol_mat)

    # back subs
    sol_mat = np.log(back_subs(coeffs, sol_mat))

    print(sol_mat)
    x_test = np.array([5, 6, 7, 8])
    y_test = sol_mat[0]*x_test + sol_mat[1]

    plt.plot(x, y, "o")
    plt.plot(x_test, y_test)
    plt.show()
