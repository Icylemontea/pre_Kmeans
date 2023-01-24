from Kmeans import *
import numpy as np
import matplotlib.pyplot as plt
import time
from dbi import comp_dbi
from pre_Kmeans import grid_pre

def show_data(file):#显示原始数据
    dataSet=loadDataSet(file)
    n=np.shape(dataSet)[0]
    for i in range(n):
        plt.plot(dataSet[i,0],dataSet[i,1],'ok')
    plt.show()


def pre_Kmeans(k,file,m=3,pre=False):#改进后的Kmeans算法，k为簇类数，file为文件路径，m为密集阈值，pre表示是否进行孤立点预处理 默认为false
    start=time.time()
    dataSet=loadDataSet(file)
    if pre==True:
        isopoint,dataSet=grid_pre(dataSet,k,m)
        centroids,clusterAssment = KMeans(dataSet,k)
        end=time.time()
        print(end-start)
        showCluster(dataSet,k,centroids,clusterAssment,isopoint)
    else:
        centroids,clusterAssment = KMeans(dataSet,k)
        end=time.time()
        print(end-start)
        showCluster(dataSet,k,centroids,clusterAssment)
        

def dbi_test(min_k,max_k,file,m,pre=False):#dbi计算方法，计算簇类数从min_k到max_k的dbi并画图，m为密集阈值，pre表示是否进行孤立点预处理 默认为false
    for i in range(min_k,max_k):
        dataSet=loadDataSet(file)
        if pre==True:
            isopoint,dataSet=grid_pre(dataSet,i,m)
        centroids,clusterAssment = KMeans(dataSet,i)
        
        plt.plot(i,comp_dbi(i,centroids,clusterAssment),'or')
    plt.show()

def dbi_test_compare(min_k,max_k,file,m):#计算簇类数从min_k到max_k的dbi并画图，将原始Kmeans和改进Kmeans进行对比并画图
    res1=[]
    res2=[]
    for i in range(min_k,max_k):
        dataSet=loadDataSet(file)
        centroids,clusterAssment = KMeans(dataSet,i)
        res1.append(comp_dbi(i,centroids,clusterAssment))
        isopoint,dataSet=grid_pre(dataSet,i,m)
        centroids,clusterAssment = KMeans(dataSet,i)
        res2.append(comp_dbi(i,centroids,clusterAssment))
    
    plt.plot(range(min_k,max_k),res1,'-or',label='Kmeans')
    plt.plot(range(min_k,max_k),res2,'-ob',label='pre_Kmeans')
    plt.legend()
    plt.show()


if __name__=="__main__":
    #show_data('test5.txt')#显示原始数据
    dbi_test_compare(3,10,'test5.txt',3)#计算dbi
    #pre_Kmeans(3,'test4.txt',m=3,pre=True)