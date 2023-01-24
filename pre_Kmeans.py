import numpy as np
import math
import Kmeans as K

def neighbor_list(i,t):
    x=i%t#网格水平分量
    y=i/t#网格竖直分量
    nlist=[]
    if x-1>=0 and y-1>=0:nlist.append(i-t-1)
    if y-1>=0:nlist.append(i-t)
    if x+1<t and y-1>=0:nlist.append(i-t+1)
    if x-1>=0:nlist.append(i-1)
    if x+1<t:nlist.append(i+1)
    if x-1>=0 and y+1<t:nlist.append(i+t-1)
    if y+1<t:nlist.append(i+t)
    if x+1<t and y+1<t:nlist.append(i+t+1)
    nlist.append(i)
    return nlist

def grid_pre(dataSet,k,m):#dataSet为输入数据集 k为用户预期聚类数 m为密度阈值
    n=np.shape(dataSet)[0]#n为数据点个数
    t=math.ceil(pow(k,1/2))#计算矩形框网格数
    isopoint=np.zeros((1,2))
    # print(np.shape(dataSet[1].reshape(1,-1)))
    # print(np.shape(isopoint))
    
    count=0
    temp=-1
    while count!=temp:
        temp=count
        maxx,maxy=np.max(dataSet,axis=0)
        minx,miny=np.min(dataSet,axis=0)
        gapx=(maxx-minx)/t
        gapy=(maxy-miny)/t
        L=0.5*pow(pow(gapx,2)+pow(gapy,2),0.5)#L为对角线长度的一半
        isopoint_no=[]
        grid_list=[]
        for i in range(pow(t,2)):#创建网格列表
            grid_list.append([0,[]])
        # extraarray=np.zeros((n,1))
        # opdata=np.append(dataSet,extraarray,axis=1)#创建用于记录数据点所在网格位置的数组
        # grip_num=np.zeros((pow(t,2),2))#G(i)数组，用于记录每个网格的数据点数量
        for i in range(n):
            if dataSet[i][0]!=minx:
                x=np.ceil((dataSet[i][0]-minx)/gapx)
            else:
                x=1
            if dataSet[i][1]!=miny:
                y=np.ceil((dataSet[i][1]-miny)/gapy)
            else:
                y=1
            grid_index=int((y-1)*t+x-1)
            grid_list[grid_index][0]+=1
            grid_list[grid_index][1].append(i)#记录每个数据点所在网格的位置
        for i in range(pow(t,2)):
            if grid_list[i][0]<=m and grid_list[i][0]!=0:
                for j in grid_list[i][1]:
                    s1=False
                    for h in neighbor_list(i,t):
                        if grid_list[h][0]>=m:
                            for f in grid_list[h][1]:
                                if j!=f and K.distEclud(dataSet[j],dataSet[f])<=L:
                                    s1=True
                                    break
                        if s1==True:
                            break
                    if s1==False:#若没有数据点在其范围内
                        # print(dataSet[j].reshape(1,-1))
                        isopoint=np.append(isopoint,dataSet[j].reshape(1,-1),axis=0)
                        isopoint_no.append(j)
                        count+=1
                        n-=1
        #按倒序将孤立点从数据集中删除
        isopoint_no.sort(reverse=True)
        for i in isopoint_no:
            dataSet=np.delete(dataSet,i,axis=0)
        # print(np.shape(dataSet))

    isopoint=np.delete(isopoint,0,axis=0)

    print(np.shape(isopoint)[0])
    return isopoint,dataSet