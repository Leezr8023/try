import numpy as np
from sklearn.linear_model import LinearRegression, RidgeCV,LassoCV, ElasticNetCV
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import random
import matplotlib.pyplot as plt
from sympy import *
def TestDataGenerate():#测试用，数据是由matlab生成的
    file = np.loadtxt('M_tab3.0.txt',dtype=np.float32,delimiter='\t')
    file_new = np.zeros(shape = (200,3))
    np.random.seed(0)
    for i in range(0,200):
        file_new[i] = file[i*100+random.randint(-75,85)]
    return np.linspace(-1,1,1600),file_new[...,2]

def newtest():
    file = np.loadtxt('M_tab.txt',dtype=np.float32,delimiter='\t')
    file_new = np.zeros(shape = (20000,1))
    for i in range(0,20000):
        file_new[i] = (file[i,1])/31417 + 2#+random.randint(-75,85)
    return np.linspace(-1,1,20000),file_new
def DataGet1():#返回可以有两种方式，一种只返回锁相的数据，位移量均匀生成
    file = np.loadtxt('data.txt',dtype=np.float32,delimiter='\t')
    return np.linspace(-1,1,200),file[...,2]

def DataGet2():#返回锁相和位移
    count = np.loadtxt('count.txt')
    title = "data/data{0}.txt".format(count-1)
    title = "data/data39.0.txt"
    file = np.loadtxt(title, dtype=np.float32, delimiter='\t')
    file_new = np.zeros(shape = (1600,2))
    for i in range(1600):
        file_new[i,0] = (file[i, 0])*1000
        file_new[i,1] = (file[i, 1])

    # plt.plot(file[0],range(1600))
    # plt.show()
    return file_new

def Datapreprocess(data):
    np.savetxt('checkdata.txt',data)
    for i in range(len(data)):
        if data[i,0]<=1.239:
        #if(abs(y[i]-y[i+1]) < 0.1):  #判别的系数需要根据实际测得数据一致
            data[i,0] = -1   #标记数据
        if (data[i,0]-1.360)>=0:
            data[i,0] = -1
    # y_new = np.setdiff1d(y,[-1])
    index = np.where(data[...,0]==-1)
    np.savetxt('checkindex.txt',index)
    # print(index)
    data_new = np.delete(data,index,0)
    # data_x = np.delete(data[...,1],index)
    np.savetxt('check.txt',data_new)
    # print(data_new)
    return data_new
# if __name__=='__main__':
#     y = DataGet2()
#
#     plt.plot(range(1600),y)
#     plt.show()
# def dd():
if __name__=='__main__':
    data = np.zeros(shape=(1600,2))
    data = DataGet2()
    N = 5
    count = 0
    models = [Pipeline([('poly', PolynomialFeatures()), ('linear', LinearRegression(fit_intercept=False,normalize = True))]),#N=16,18
              Pipeline([('poly', PolynomialFeatures()),
                        ('linear', RidgeCV(alphas=np.logspace(-3, 2, 50), fit_intercept=False,normalize=True))])]
    for k in range(4):
        data_quarter = data[int(len(data)*k/4):int(len(data)*(k+1)/4),...]
        data_new = Datapreprocess(data_quarter)
        x = data_new[...,1]
        y = data_new[...,0]
        x.shape = -1, 1
        y.shape = -1, 1
        model = models[1]
        model.set_params(poly__degree=N)
        model.fit(x, y.ravel())
        lin = model.get_params('linear')['linear']
        # print("lin.coef_.ravel():\n", lin.coef_.ravel())#系数输出
        x_hat = np.linspace(x.min(), x.max(), num=len(y))
        x_hat.shape = -1, 1
        y_hat = model.predict(x_hat)
        dify1 = np.diff(y_hat)
        dify2 = np.diff(dify1)
        index = np.where(dify2 == max(dify2))

        # M_max = max(y)
        # M_min = min(y)
        # print(M_max)
        # print(M_min)
        r0 = 1.360-(1.360-1.23)*0.8# (M_max + M_min)/2
        # r0 = 5/2
        index1 = np.where(abs(y-r0)<0.01)#判断相等，0.001时LassoCV无结果，ElasticNetCV正常
        avg = np.mean(x[index1])

        print(avg)
        # print(x[index1])
        print(x[index])
        print(abs(avg-x[index]))
        # print(abs(x[0]-x[index]))
        print("")
        count = count + abs(avg-x[index])
        # plt.plot(x, y)
        # plt.plot(x_hat, y_hat)
        # plt.show()
    print(count/2)


def qtoutput():
    data = np.zeros(shape=(1600,2))
    data = DataGet2()
    N = 5
    count = 0
    models = [Pipeline([('poly', PolynomialFeatures()), ('linear', LinearRegression(fit_intercept=False,normalize = True))]),#N=16,18
              Pipeline([('poly', PolynomialFeatures()),
                        ('linear', RidgeCV(alphas=np.logspace(-3, 2, 50), fit_intercept=False,normalize=True))])]
    for k in range(4):
        data_quarter = data[int(len(data)*k/4):int(len(data)*(k+1)/4),...]
        data_new = Datapreprocess(data_quarter)
        x = data_new[...,1]
        y = data_new[...,0]
        x.shape = -1, 1
        y.shape = -1, 1
        model = models[1]
        model.set_params(poly__degree=N)
        model.fit(x, y.ravel())
        lin = model.get_params('linear')['linear']
        # print("lin.coef_.ravel():\n", lin.coef_.ravel())#系数输出
        x_hat = np.linspace(x.min(), x.max(), num=len(y))
        x_hat.shape = -1, 1
        y_hat = model.predict(x_hat)
        dify1 = np.diff(y_hat)
        dify2 = np.diff(dify1)
        index = np.where(dify2 == max(dify2))

        # M_max = max(y)
        # M_min = min(y)
        # print(M_max)
        # print(M_min)
        r0 = 1.360-(1.36-1.275)*0.8# (M_max + M_min)/2
        # r0 = 5/2
        index1 = np.where(abs(y-r0)<0.01)#判断相等，0.001时LassoCV无结果，ElasticNetCV正常
        avg = np.mean(x[index1])

        print(avg)
        # print(x[index1])
        print(x[index])
        print(abs(avg-x[index]))
        # print(abs(x[0]-x[index]))
        print("")
        count = count + abs(avg-x[index])
        # plt.plot(x, y)
        # plt.plot(x_hat, y_hat)
        # plt.show()
    print(count/2)
    return float(count/2)

