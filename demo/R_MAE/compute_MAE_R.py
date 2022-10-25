import argparse
import math
import pandas as pd
import numpy as np


parser = argparse.ArgumentParser(description='analyse gb/pbsa data')
parser.add_argument('-i1', type=str, help='first data file')
parser.add_argument('-i2', type=str, help='second data file')
parser.add_argument('-i3', type=str, help='third data file')
parser.add_argument('-e', type=str, help='experiment data file')
parser.add_argument('-o', type=str, help='output file',default="result.txt")
args = parser.parse_args()

def computeCorrelation(X, Y):
    xBar = np.mean(X)
    yBar = np.mean(Y)
    SSR = 0
    varX = 0
    varY = 0
    for i in range(0 , len(X)):
        diffXXBar = X[i] - xBar
        diffYYBar = Y[i] - yBar
        SSR += (diffXXBar * diffYYBar)
        varX +=  diffXXBar**2
        varY += diffYYBar**2
    
    SST = math.sqrt(varX * varY)
    return SSR / SST

def computeMAE(X, Y):
    error=0
    for i in range(0 , len(X)):
        error=abs(X[i]-Y[i])+error
    return error/len(X)


def total(exp,pred):
    X = np.array([float(i) for i in exp])
    Y = np.array([float(i) for i in pred])
    poly = np.polyfit(X, Y, deg=1)
    Y_trans=[]
    for y in Y:
        diff=y-poly[1]
        Y_trans.append(diff/poly[0])
    mae=computeMAE(X,Y_trans)
    R=computeCorrelation(X,Y_trans)
    return round(poly[0],2), round(poly[1],2), round(R,2), round(mae,2)


#read data
data=(np.loadtxt(args.i1)+np.loadtxt(args.i2)+np.loadtxt(args.i3))/3
#print(data)
ex=np.loadtxt(args.e)
df = pd.DataFrame(data)
df.columns=["index","GBSA","PBSA"]
df["EXP"]=ex
#gbsa
gbsa=total(df["EXP"],df["GBSA"])
print("A,B,R,MAE for GBSA calculation....")
#pbda
pbsa=total(df["EXP"],df["PBSA"])
print("A,B,R,MAE for PBSA calculation....")

final=pd.DataFrame([gbsa,pbsa])
final.columns=["A","B","R","MAE"]
final.index=["gbsa","pbsa"]
print(final)
final.to_csv(args.o)
