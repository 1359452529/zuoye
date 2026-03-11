import sys
sys.path.append("./src")
from eight_queens import is_safe, solve_eight_queens

def test_is_safe():
    # 测试初始位置安全
    board = [-1] * 8
    assert is_safe(board, 0, 0) is True
    # 测试同列冲突
    board[0] = 1
    assert is_safe(board, 1, 1) is False

def test_solve_count():
    # 验证八皇后解数为92
    assert len(solve_eight_queens(8)) == 92

def test_edge():
    # 测试边界情况
    assert len(solve_eight_queens(1)) == 1  # 1皇后有1个解
    assert len(solve_eight_queens(2)) == 0  # 2皇后无解
    assert len(solve_eight_queens(3)) == 0  # 3皇后无解
