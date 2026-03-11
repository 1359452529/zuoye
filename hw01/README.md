# 八皇后工程化实践
## 项目结构
hw01/
├── src/eight_queens.py  # 求解器
└── tests/test_eight_queens.py  # 测试

## 运行
python src/eight_queens.py

## 测试
pytest tests/test_eight_queens.py -v

## 实现思路
使用回溯法逐行放置皇后，检查列、两条对角线是否冲突，找到所有合法解。