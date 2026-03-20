#作用：fixture,hooks,全局变量，pytest自动发现及加载

import os
import sys 

# pytest 默认会把 tests/ 所在目录加入 sys.path，但有时（例如从上级目录运行、或 CI 环境）可能不包含项目根，导致 import core 失败。
# 在 conftest.py 里显式插入项目根，可以保证无论从哪里执行 pytest，都能正确导入 core 包。

sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))