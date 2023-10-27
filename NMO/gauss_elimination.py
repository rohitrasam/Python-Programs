from numpy import array, zeros_like

def rref():
    for i in range(a_rows-1):
        for j in range(i+1, a_rows):
            if a[i, i] != 1:
                b[i] /= a[i, i]
                a[i, :] /= a[i, i]
            
            b[j] -= a[j, i] * b[i]
            a[j, :] -= a[j, i] * a[i, :]

def back_subs():
    x[-1] = b[-1]/a[-1, -1]
    for k in range(x_rows-2, -1, -1):
        x[k] = b[k]
        for l in range(k, x_rows-1):
           x[k] -= a[k, l+1] * x[l+1] 

n = int(input("Enter number of equations: "))
# Initialize matrix
print("Enter the coefficient matrix:")
# For user input
a = array([[x for x in input().split()] for y in range(n)], float)
print(f"Your matrix is\n{a}")
print("Enter `b` matrix: ", end=' ')
b = array([y for y in input().split()], float).reshape((n, 1))
print(f"The `b` matrix is\n{b}")
x = zeros_like(b)

a_rows = a.shape[0]
x_rows = x.shape[0]

# Elimination
rref()

# Back substitution
back_subs()

print(f"The solution matrix is\n{x.round(2)}")
