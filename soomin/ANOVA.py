import sys
import os
sys.path.append("../func")
from d0_makelist import MakeList
#filename = ("../data_txt/ALL_DATA/Aqi_Beijing_monthly.txt")
filename = ("../data_txt/ALL_DATA/Aqi_Beijing_WIND.txt")
list_A  = MakeList(filename)
import scipy.stats as stats
'''
a=[28,24,22,23,28]
b=[24,22,28,22,24]
c=[21,20,21,23,20]


ANOVA = stats.f_oneway(a,b,c)
print(ANOVA)
'''
#print(list_A)

Y2014 = []
Y2015 = []
Y2016 = []
Y2017 = []
Y2018 = []
year=201400
print(list_A[0])
for ii in range(len(list_A)):
    if ii == 0:
        continue
    elif float(list_A[ii][0])<20140000:
        continue
    elif 20140000<float(list_A[ii][0])<20150000:
        Y2014.append(list_A[ii])
    elif 20150000<float(list_A[ii][0])<20160000:
        Y2015.append(list_A[ii])
    elif 20160000<float(list_A[ii][0])<20170000:
        Y2016.append(list_A[ii])
    elif 20170000<float(list_A[ii][0])<20180000:
        Y2017.append(list_A[ii])
    elif 20180000<float(list_A[ii][0]):
        Y2018.append(list_A[ii])

Y2014.append(list_A[0]);Y2015.append(list_A[0]);Y2016.append(list_A[0])
Y2017.append(list_A[0]);Y2018.append(list_A[0])    
        
#print(Y2014);print(Y2015);print(Y2016);print(Y2017);print(Y2018)

AQI_A = [];AQI_B=[];AQI_C=[];AQI_D=[];AQI_E=[]

for aa in range(len(list_A)):
    if aa==0:
        continue
    elif float(list_A[aa][0])<20150000:
        AQI_A.append(list_A[aa][1])
    elif 20150000<float(list_A[aa][0])<20160000:
        AQI_B.append(list_A[aa][1])
    elif 20160000<float(list_A[aa][0])<20170000:
        AQI_C.append(list_A[aa][1])
    elif 20170000<float(list_A[aa][0])<20180000:
        AQI_D.append(list_A[aa][1])
    elif 20180000<float(list_A[aa][0]):
        AQI_E.append(list_A[aa][1])
print(AQI_A)
print(AQI_B)

ANOVA = stats.f_oneway(AQI_A,AQI_B,AQI_C,AQI_D,AQI_E)
print(ANOVA)
