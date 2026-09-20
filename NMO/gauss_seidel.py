import numpy as np

n = int(input("Enter number of equations: "))

print("Enter coefficient matrix:")
a = np.array([input().split() for _ in range(n)], dtype=np.float32)
print(f"Coeff matrix:\n{a}")

print("Enter solution matrix:")
b = np.array(input().split(), dtype=np.float32).reshape(-1, 1)


rows, cols = a.shape

for i in range(cols-1):
    mx = a[:, i].argmax()
    a[[mx, i]] = a[[i, mx]]
    b[[mx, i]] = b[[i, mx]]
print(a)
print(b)


x1 = np.zeros_like(b)

print(x1)
iter = True if input("Iterations or accuracy(I or A)? ") == "I" else False 
for i in range(rows):
    x1[i] = (b[i] - a[i, (i+1)%rows]*x1[(i+1)%rows] - a[i, (i+2)%rows]*x1[(i+2)%rows])/a[i, i] 

if not iter:
    acc = float(input("Enter required accuracy: "))
    x2 = np.zeros_like(b)
    print(x2)
    while not (abs(x2-x1) < acc).all():
        x2 = x1
        for i in range(rows):
            x1[i] = (b[i] - a[i, (i+1)%rows]*x1[(i+1)%rows] - a[i, (i+2)%rows]*x1[(i+2)%rows])/a[i, i]
else:
    n = int(input("Enter number of iterations: "))
    for i in range(n):
        for i in range(rows):
            x1[i] = (b[i] - a[i, (i+1)%rows]*x1[(i+1)%rows] - a[i, (i+2)%rows]*x1[(i+2)%rows])/a[i, i]
    
print(x1.round(4))