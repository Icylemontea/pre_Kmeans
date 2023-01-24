# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:57:22 2019

@author: muli
"""
#将mat文件转换为txt
import scipy.io as scio
 
path = 'label_excel.mat'
data = scio.loadmat('cluster_data/five_cluster.mat')
# 查看mat文件的数据格式
#<class 'dict'>
print(type(data) ) 
                    
#查看字典的键
#dict_keys(['__header__', '__version__', '__globals__', 'bags', 'targets', 'class_name'])
print(data.keys() )             

#dict_keys(['__header__', '__version__', '__globals__', 'X', 'y'])

#选择需要的数据；数组格式
x = data['x']         

f2=open('text5.txt',mode='a')
for j in range(2001):
    f2.write(str(x[0][j])+" ")
    f2.write(str(x[1][j]))
    f2.write("\n")        

f2.close()

