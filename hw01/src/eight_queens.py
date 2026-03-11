def is_safe(board, row, col, n=8):
    # 检查同一列是否有皇后
    for i in range(row):
        if board[i] == col:
            return False
    # 检查左上到右下对角线
    for i, j in enumerate(range(row-1, -1, -1)):
        if board[j] == col - (i + 1):
            return False
    # 检查右上到左下对角线
    for i, j in enumerate(range(row-1, -1, -1)):
        if board[j] == col + (i + 1):
            return False
    return True

def solve_eight_queens(n=8):
    solutions = []
    def backtrack(row, current_board):
        if row == n:
            solutions.append(current_board.copy())
            return
        for col in range(n):
            if is_safe(current_board, row, col, n):
                current_board[row] = col
                backtrack(row + 1, current_board)
                current_board[row] = -1  # 回溯
    
    initial_board = [-1] * n
    backtrack(0, initial_board)
    return solutions

def print_solution(solution):
    n = len(solution)
    for row in range(n):
        line = ["." for _ in range(n)]
        line[solution[row]] = "Q"
        print(" ".join(line))
    print("-" * (2 * n - 1))

if __name__ == "__main__":
    solutions = solve_eight_queens()
    print(f"八皇后共有 {len(solutions)} 个解")
    print_solution(solutions[0])
