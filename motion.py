import SR830
import XPS
import numpy as np
from const import START_POSITION,FINISH_ONCE,\
    SECEND_START,SECEND_FINISH,data,STEP,exitFlag,single_num

global exitFlag
def startmeasure():
    sr = SR830.SR830()
    xps = XPS.MyXPS()
    sr.setIT(i=19)
    sr.setSens(i=24)


    xps.measureMove(START_POSITION)
    for i in range(0, 100):
        xps.measureMove(START_POSITION + STEP * i)
        postion = xps.GetPosition()
        sum = 0.0
        for k in range(single_num):
            res = sr.getOut(3)
            sum = sum + res
        data[i, 0] = sum/single_num
        data[i, 1] = postion

    xps.measureMove(SECEND_START)
    for i in range(100, 200):
        xps.measureMove(SECEND_START + STEP * i)
        postion = xps.GetPosition()
        sum = 0.0
        for k in range(single_num):
            res = sr.getOut(3)
            # print(res)
            sum = sum + res
        data[i, 0] = sum/single_num
        data[i, 1] = postion

    xps.measureMove(SECEND_FINISH)
    for i in range(200,300):
        xps.measureMove(SECEND_FINISH - i * STEP)
        postion = xps.GetPosition()
        sum = 0.0
        for k in range(single_num):
            res = sr.getOut(3)
            # print(res)
            sum = sum + res
        data[i, 0] = sum/single_num
        data[i, 1] = postion

    xps.measureMove(FINISH_ONCE)
    for i in range(300,400):
        xps.measureMove(FINISH_ONCE - i * STEP)
        postion = xps.GetPosition()
        sum = 0.0
        for k in range(single_num):
            res = sr.getOut(3)
            # print(res)
            sum = sum + res
        data[i, 0] = sum/single_num
        data[i, 1] = postion

    sr.close()
    xps.close()
    # print(data)
    num = np.loadtxt('count.txt')
    title = "data/data{0}.txt".format(num)
    np.savetxt(title, data, fmt='%f', delimiter='\t')
    np.savetxt("count.txt",[num+1])
    exitFlag[0] = 1
    print("shebei:")
    print(exitFlag[0])
