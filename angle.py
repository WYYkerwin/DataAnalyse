import re
import numpy as np
import string
import csv
import pandas as pd
import xlwt
from xlutils.copy import copy
import xlrd
import os
import math
import codecs


f = codecs.open('DataRecord.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8'编码读取
line = f.readline()  # 以行的形式进行读取文件
#print(line)

DirX=[]
DirY=[]
DirZ=[]
Time=[]
PosX=[]
PosY=[]
PosZ=[]

while line:

    Origin =line[0:15]
    #print(Origin)

    line1 = line.partition("x")
    line2 =line1[2]

    line3 = line2.partition("y")

    DirX1= line3[0]

    line4 =line3[2]
    line5=line4.partition("z")

    DirY1= line5[0]

    line6=line5[2]
    line7=line6.partition("//")

    DirZ1=line7[0]

    line8=line7[2]
    line9=line8.partition("CurrentSystemTime(ms): ")

    line10=line9[2]
    line11=line10.partition("     FocusPosition:")

    time=line11[0]

    line12=line11[2]
    line13=line12.partition("(")

    line14=line13[2]
    line15=line14.partition(", ")

    posx=line15[0]
    line16=line15[2]
    line17=line16.partition(", ")

    posy = line17[0]

    line18=line17[2]
    line19=line18.partition(")")

    posz=line19[0]


    DirX.append(DirX1)
    DirY.append(DirY1)
    DirZ.append(DirZ1)
    Time.append(time)
    PosX.append(posx)
    PosY.append(posy)
    PosZ.append(posz)

    line = f.readline()
f.close()



AV=[]
Nummax=0
for b in DirX:
    Nummax=Nummax+1
# print(Nummax)
# print(Time)
#
i=1
for a in DirX:
    if i<Nummax-1:
        a1=float(DirX[i])
        a2=float(DirY[i])
        a3=float(DirZ[i])
        b1=float(DirX[i+1])
        b2=float(DirY[i+1])
        b3=float(DirZ[i+1])
        time1=float(Time[i])
        time2=float(Time[i+1])

        TimeDif=time2-time1

        COS=(a1*b1+a2*b2+a3*b3)/np.sqrt(math.pow( a1, 2 )+math.pow( a2, 2 )+math.pow( a3, 2 ))*np.sqrt(math.pow( b1, 2 )+math.pow( b2, 2 )+math.pow( b3, 2 ))
        angle=math.degrees(math.acos(COS))

        VA=(angle/TimeDif)*1000

        #print(VA)
        AV.append(VA)
        i=i+1
#print(AV)


mvmts = []  # length is len(data)-1

for v in AV:
    if (v < 30):
        # fixation
        mvmts.append(1)
    # print v, v_threshold
    else:
        mvmts.append(0)
#print(mvmts)

fixations = []
fs = []

# print mvmts

for m in range(len(mvmts)):
    if (mvmts[m] == 0):
        if (len(fs) > 0):
            fixations.append(fs)
            fs = []
    else:
        fs.append(m)
if (len(fs) > 0):
    fixations.append(fs)

#print(fixations)

centroidsX = []
centroidsY = []
centroidsZ = []
time0 = []
time1 = []
Duration=[]


for f in fixations:
    cX = 0
    cY = 0
    cZ = 0

    if (len(f) == 1):
        i = f[0]+1
        cX = (float(PosX[i]) + float(PosX[i + 1])) / 2.0
        cY = (float(PosY[i]) + float(PosY[i + 1])) / 2.0
        cZ = (float(PosZ[i]) + float(PosZ[i + 1])) / 2.0

        t0 = float(Time[i])
        t1 = float(Time[i + 1])

    else:
        t0 = float(Time[f[0]+1])
        t1 = float(Time[f[len(f) - 1] + 1+1])

        for e in range(len(f)):
            cX += float(PosX[f[e]+1])
            cY += float(PosY[f[e]+1])
            cZ += float(PosZ[f[e]+1])

        cX += float(PosX[f[len(f) - 1] + 1+1])
        cY += float(PosY[f[len(f) - 1] + 1+1])
        cZ += float(PosZ[f[len(f) - 1] + 1+1])

        cX = cX / float(len(f) + 1)
        cY = cY / float(len(f) + 1)
        cZ = cZ / float(len(f) + 1)
    centroidsX.append(cX)
    centroidsY.append(cY)
    centroidsZ.append(cZ)
    time0.append(t0)
    time1.append(t1)
    time3=t1-t0
    Duration.append(time3)

# print(centroidsX)
# print(centroidsY)
# print(centroidsZ)
# print(time0)
# print(time1)

DA = pd.DataFrame([centroidsX,centroidsY,centroidsZ,time0,time1,Duration])
DA1=pd.DataFrame(DA.values.T, index=DA.columns, columns=DA.index)
DA1.drop(index=(DA1.loc[(DA1[5]<100)].index),inplace=True)
print(DA1)

Data = DA1.values.tolist()
#print(Data)
name=['centroidsX','centroidsY','centroidsZ','time0','time1','Duration']
test=pd.DataFrame(columns=name,data=Data)#数据有三列，列名分别为one,two,three
#print(test)
test.to_csv('D:\清华实验\DataAnalyse/CaptureData.csv',encoding='gbk')







