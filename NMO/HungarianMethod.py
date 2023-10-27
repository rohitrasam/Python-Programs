import numpy as np

def minimization(mat: np.ndarray):

    def row_minimization():
        for row in range(mat.shape[0]):
            mat[row] -= np.min(mat[row])
    
    def column_minimization():
        for col in range(mat.shape[1]):
            mat[:, col] -= np.min(mat[:, col])


    row_minimization()
    print(mat)
    column_minimization()
    print(mat)

    return mat    



if __name__ == '__main__':
    rows, cols = map(int, input("Enter number of rows and cols: ").split())
    mat = np.zeros((rows, cols))
    for row in range(rows):
        row_values = list(map(float, input("Enter the row values: ").split()))
        mat[row] = row_values
    print(mat)
    result = minimization(mat)
    print(result)