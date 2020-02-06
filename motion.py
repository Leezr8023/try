import SR830
import XPS
import time
import numpy as np
from const import START_POSITION,FINISH_ONCE,\
    SECEND_START,SECEND_FINISH,data,STEP,exitFlag,single_num,point_num
# min_light,max_light

global exitFlag
global START_POSITION
global FINISH_ONCE
global SECEND_START
global SECEND_FINISH
global data
global STEP
global point_num
global single_num
# global min_light
# global max_light

def startmeasure():
    sr = SR830.SR830()
    xps = XPS.MyXPS()
    sr.setIT(i=19)
    sr.setSens(i=24)
    # xps.measureMove(0)
    # light = np.zeros(shape=(100,1))
    # for i in range(100):
    #     res = sr.getOut(3)
    #     light[i] = res
    # min_light = max(light)
    # time.sleep(5)
    # xps.measureMove(12)
    # for i in range(100):
    #     res = sr.getOut(3)
    #     light[i] = res
    # max_light = min(light)
    # time.sleep(5)
    xps.measureMove(START_POSITION)
    for i in range(0, 400):
        xps.measureMove(START_POSITION + STEP * i)
        postion = xps.GetPosition()
        # print(postion)
        sum = 0.0
        for k in range(single_num):
            res = sr.getOut(3)
            sum = sum + res
        data[i, 0] = sum/single_num
        # print(i)
        data[i, 1] = abs(postion - START_POSITION)

    xps.measureMove(SECEND_START)
    for i in range(400, 800):
        xps.measureMove(SECEND_START + STEP * (i-400))
        postion = xps.GetPosition()
        sum = 0.0
        for k in range(single_num):
            res = sr.getOut(3)
            sum = sum + res
        data[i, 0] = sum/single_num
        data[i, 1] = abs(postion-SECEND_START)

    xps.measureMove(SECEND_FINISH)
    for i in range(800,1200):
        xps.measureMove(SECEND_FINISH - (i-800) * STEP)
        postion = xps.GetPosition()
        sum = 0.0
        for k in range(single_num):
            res = sr.getOut(3)
            sum = sum + res
        data[i, 0] = sum/single_num
        data[i, 1] = abs(postion-SECEND_FINISH)

    xps.measureMove(FINISH_ONCE)
    for i in range(1200,1600):
        xps.measureMove(FINISH_ONCE - (i-1200) * STEP)
        postion = xps.GetPosition()
        sum = 0.0
        for k in range(single_num):
            res = sr.getOut(3)
            sum = sum + res
        data[i, 0] = sum/single_num
        data[i, 1] = abs(postion-FINISH_ONCE)

    sr.close()
    xps.close()
    num = np.loadtxt('count.txt')
    title = "data/data{0}.txt".format(num)
    np.savetxt(title, data, fmt='%f', delimiter='\t')
    np.savetxt("count.txt",[num+1])
    exitFlag[0] = 1
