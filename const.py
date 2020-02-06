import numpy as np
# file = np.loadtxt('setting.txt',dtype=np.float32,delimiter='\n')
# 刀头四点
# START_POSITION = file[0]
# # FINISH_ONCE = file[1]
# # SECEND_START = file[2]
# # SECEND_FINISH = file[3]
# #
# # # 步长
# # STEP = file[4]# 0.00001  10nm
# #
# # point_num = file[5].astype(int)
# #
# # delay = file[6]
# #
# # y_range = [file[7],file[8]]
# #
# # single_num = file[9].astype(int)
# # # 画图信号
# # SIGNAL = 1
# # # 线程退出信号
# # exitFlag = [0]
START_POSITION = -12.0
FINISH_ONCE = -8.0
SECEND_START = 0.0
SECEND_FINISH = 4.0

# 步长
STEP = 0.01# 0.00001  10nm

point_num = 1600

delay = 0.5

y_range = [0.0010,0.0015]

single_num = 6
# 画图信号
SIGNAL = 1
# 线程退出信号
exitFlag = [0]

data = np.zeros(shape=(point_num, 2))
# print(file)
# print(START_POSITION)
# print(FINISH_ONCE)
# print(SECEND_START)
# print(SECEND_FINISH)
# print(STEP)
# print(point_num)
# print(delay)
# print(y_range)
# print(single_num)

# min_light = 0
# max_light = 0

