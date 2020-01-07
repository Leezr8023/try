import numpy as np
# 刀头四点
START_POSITION = 0
FINISH_ONCE = 0.1
SECEND_START = 10
SECEND_FINISH = 10.1

# 步长
STEP = 0.001# 0.00001  10nm

# 画图信号
SIGNAL = 1
# 线程退出信号
exitFlag = 0

data = np.zeros(shape=(400, 2))