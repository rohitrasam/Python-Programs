import numpy as np

def rref(coeff_matrix, sol_matrix):
    
    rows = coeff_matrix.shape[0]
    for i in range(rows):
        sol_matrix[i] /= coeff_matrix[i, i]
        coeff_matrix[i, :] /= coeff_matrix[i, i]
        for j in range(i+1, rows):
            sol_matrix[j] -= sol_matrix[i]*coeff_matrix[j, i]
            coeff_matrix[j, :] -= coeff_matrix[i, :]*coeff_matrix[j, i]
    
    return coeff_matrix, sol_matrix

def back_subs(coeff_matrix, sol_matrix):

    rows = coeff_matrix.shape[0]
    for i in range(rows-2, -1, -1):
        for j in range(i+1, rows):
            sol_matrix[i] -= sol_matrix[j]*coeff_matrix[i, j]
    
    return sol_matrix




if __name__ == '__main__':


    n = int(input("Enter number of equations: "))

    print("Enter coefficient matrix: ")
    a = np.array([input().split() for _ in range(n)], dtype=np.float32)
    print("Enter solution matrix: ")
    b = np.array([x for x in input().split()], dtype=np.float32).reshape(-1, 1)
    print("Your matrices are: ")
    print(f"{a}\n{b}")

    rows = a.shape[0]

    a, b = rref(a, b)
    print("After row transformations: ")
    print(np.hstack((a, b)))


    b = back_subs(a, b)
    print(f"After back substitutions your soultion vector is :\n{b.round(4)}")