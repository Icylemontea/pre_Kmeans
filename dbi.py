#y用于计算dbi的代码
import numpy as np

def distEclud(x,y):
    return np.sqrt(np.sum((x-y)**2))  # 计算欧氏距离

def comp_si(f,clusterAssment):#f为所属簇的编号
    n=np.shape(clusterAssment)[0]
    t=0
    sum=0
    for i in range(n):
        if f==clusterAssment[i,0]:
            t+=1
            sum+=clusterAssment[i,1]
    if t==0:return 0
    return pow(sum/t,0.5)

def comp_mij(f,g,centroids):#f,g为两类的质心编号
    return distEclud(centroids[f],centroids[g])

def comp_rij(f,g,centroids,clusterAssment):
    return (comp_si(f,clusterAssment)+comp_si(g,clusterAssment))/comp_mij(f,g,centroids)

def comp_dbi(k,centroids,clusterAssment):#k为总类数
    for i in range(k-1):
        d=0
        sum=0
        for j in range(i+1,k):
            d=max(d,comp_rij(i,j,centroids,clusterAssment))
            if d<0:print(centroids[i],centroids[j])
        sum+=d
    return d/k
