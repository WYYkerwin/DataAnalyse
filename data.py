import re
import numpy as np
import string
import csv
import pandas as pd
import xlwt
from xlutils.copy import copy
import xlrd
import math
impo/rt codecs

f = codecs.open('111Record.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8'编码读取
line = f.readline()  # 以行的形式进行读取文件
#print(line)

DX=[]
DY=[]
DZ=[]
Time=[]
PX=[]
PY=[]
PZ=[]

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


    DX.append(DirX1)
    DY.append(DirY1)
    DZ.append(DirZ1)
    Time.append(time)
    PX.append(posx)
    PY.append(posy)
    PZ.append(posz)

    line = f.readline()
f.close()



AV=[]
Nummax=0
for b in DX:
    Nummax=Nummax+1
#print(Nummax)


i=3
for a in DX:
    if i<Nummax-1:
        a1=float(DX[i])
        a2=float(DY[i])
        a3=float(DZ[i])
        b1=float(DX[i+1])
        b2=float(DY[i+1])
        b3=float(DZ[i+1])
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

print(fixations)
print(PX)
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
        i = f[0]+3
        cX = (float(PX[i]) + float(PX[i + 1])) / 2.0
        cY = (float(PY[i]) + float(PY[i + 1])) / 2.0
        cZ = (float(PZ[i]) + float(PZ[i + 1])) / 2.0

        t0 = float(Time[i])
        t1 = float(Time[i + 1])

    else:
        t0 = float(Time[f[0]+3])
        t1 = float(Time[f[len(f) - 1] + 1+3])

        for e in range(len(f)):
            cX += float(PX[f[e]+3])
            cY += float(PY[f[e]+3])
            cZ += float(PZ[f[e]+3])

        cX += float(PX[f[len(f) - 1] + 1+3])
        cY += float(PY[f[len(f) - 1] + 1+3])
        cZ += float(PZ[f[len(f) - 1] + 1+3])

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

print(centroidsX)
print(centroidsY)
print(centroidsZ)
# print(time0)
# print(time1)

DA = pd.DataFrame([centroidsX,centroidsY,centroidsZ,time0,time1,Duration])
DA1=pd.DataFrame(DA.values.T, index=DA.columns, columns=DA.index)

Data = DA1.values.tolist()
print(Data)
name=['centroidsX','centroidsY','centroidsZ','time0','time1','Duration']
test=pd.DataFrame(columns=name,data=Data)#数据有三列，列名分别为one,two,three
print(test)
test.to_csv('D:\清华实验\DataAnalyse/data.csv',encoding='gbk')







