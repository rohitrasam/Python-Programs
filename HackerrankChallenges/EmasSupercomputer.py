def twoPluses(grid: list[str]):
    grid = list(map(list, grid))

    answer = 0
    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[row])-1):
            cells = 0
            while ((row + cells < len(grid) and col + cells < len(grid[row]) and row-cells >= 0 and col - cells >= 0) and 
                    grid[row-cells][col] == 'G' and 
                    grid[row+cells][col] == 'G' and 
                    grid[row][col-cells] == 'G' and 
                    grid[row][col+cells] == 'G'):
                
                grid[row-cells][col] = grid[row+cells][col] = grid[row][col-cells] = grid[row][col+cells] = 'g'

                for ROW in range(1, len(grid)-1):
                    for COL in range(1, len(grid[ROW])-1):
                        CELLS = 0
                        while ((ROW + CELLS < len(grid) and COL + CELLS < len(grid[ROW]) and ROW-CELLS >= 0 and COL - CELLS >= 0) and 
                    grid[ROW-CELLS][COL] == 'G' and 
                    grid[ROW+CELLS][COL] == 'G' and 
                    grid[ROW][COL-CELLS] == 'G' and 
                    grid[ROW][COL+CELLS] == 'G'):
                            answer = max(answer, (4*cells + 1)* (4*CELLS + 1))
                            CELLS += 1

                cells += 1
            cells = 0
            while ((row + cells < len(grid) and col + cells < len(grid[row]) and row-cells >= 0 and col - cells >= 0) and 
                    grid[row-cells][col] == 'g' and 
                    grid[row+cells][col] == 'g' and 
                    grid[row][col-cells] == 'g' and 
                    grid[row][col+cells] == 'g'):
                
                grid[row-cells][col] = grid[row+cells][col] = grid[row][col-cells] = grid[row][col+cells] = 'G'
                cells += 1 

    return answer

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    grid = []

    for _ in range(n):
        item = input()
        grid.append(item)
    
    result = twoPluses(grid)
    print(result)