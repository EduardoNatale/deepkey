from django.shortcuts import render
import csv
import pandas as pd
import numpy as np
from scipy import spatial

def deepkey(request):
    if request.method == 'POST':
        if request.POST.get('input-password', None) == 'qwerty123':
            # table1 = brokenData(request.POST.get('inputTable1', None), 3)
            # table2 = brokenData(request.POST.get('inputTable2', None), 3)
            # table3 = brokenData(request.POST.get('inputTable3', None), 3)
            #
            # with open('tabela1.csv', 'a') as csv1:
            #     writer = csv.writer(csv1)
            #     writer.writerows(table1)
            # with open('tabela2.csv', 'a') as csv2:
            #     writer = csv.writer(csv2)
            #     writer.writerows(table2)
            # with open('tabela3.csv', 'a') as csv3:
            #     writer = csv.writer(csv3)
            #     writer.writerows(table3)

            # transformInformation()

            if len(brokenData(request.POST.get('inputTable3', None), 3)) == 18:
                du, uu, dd = tranformInformationWCsv(brokenData(request.POST.get('inputTable3', None), 3))
                ddu, duu, ddd = verifyItself(du, uu, dd)

                if ddu >= 0.98 and ddu >= 0.97 and ddd >= 0.96:
                    return render(request, 'index.html', {'message': 'Bem vindo'})
                else:
                    return render(request, 'index.html', {'error': 'Você não é quem diz ser'})
            else:
                return render(request, 'index.html', {'error': 'Digite a sua senha sem errar'})
        else:
            return render(request, 'index.html', {'error': 'Senha incorreta'})

    return render(request, 'index.html')

def brokenData(data, n):
    listinha = []
    listona = []
    data = data.split(',')
    for i in data:
        listinha.append(i)
        if len(listinha) == n:
            listona.append(listinha)
            listinha = []

    return listona

def transformInformation():
    df = pd.read_csv('tabela3.csv', header=None)

    lData = []
    mData = []
    mmData = []
    for row in df.iterrows():
        index, data = row

        if data[0] == 0 and index != 0:
            lData.append(mData)
            mData = []
        mmData = []
        for value in data:
            mmData.append(value)
        mData.append(mmData)

        if index == len(df) - 1:
            lData.append(mData)

    du = ['DU1', 'DU2', 'DU3', 'DU4', 'DU5', 'DU6', 'DU7', 'DU8', 'DU9']
    dd = ['DD1', 'DD2', 'DD3', 'DD4', 'DD5', 'DD6', 'DD7', 'DD8']
    uu = ['UU1', 'UU2', 'UU3', 'UU4', 'UU5', 'UU6', 'UU7', 'UU8']

    du_df = pd.DataFrame(columns=du)
    dd_df = pd.DataFrame(columns=dd)
    uu_df = pd.DataFrame(columns=uu)

    for first in lData:
        duData = []
        uuData = []
        ddData = []

        chunkUP = []
        chunkDOWN = []

        if len(first) == 18:
            for second in first:
                if second[2] == "UP":
                    chunkUP.append(second)
                if second[2] == "DOWN":
                    chunkDOWN.append(second)

            for i in range(9):
                up = chunkUP[i][1]
                down = chunkDOWN[i][1]
                duData.append(up - down)

                if i < 8:
                    up_1 = chunkUP[i + 1][1]
                    down_1 = chunkDOWN[i + 1][1]
                    uuData.append(up_1 - up)
                    ddData.append(down_1 - down)

            du_df.loc[len(du_df)] = duData
            dd_df.loc[len(dd_df)] = ddData
            uu_df.loc[len(uu_df)] = uuData

    du_df.to_csv('du.csv')
    dd_df.to_csv('dd.csv')
    uu_df.to_csv('uu.csv')

def verifyItself(duData, uuData, ddData):
    dd = pd.read_csv('dd.csv', header=None)
    du = pd.read_csv('du.csv', header=None)
    uu = pd.read_csv('uu.csv', header=None)

    ddOriginalUser = treatData(dd)
    duOriginalUser = treatData(du)
    uuOriginalUser = treatData(uu)

    ddOriginalUser = np.array(ddOriginalUser).mean(axis=0)
    duOriginalUser = np.array(duOriginalUser).mean(axis=0)
    uuOriginalUser = np.array(uuOriginalUser).mean(axis=0)

    ddUser = np.array(ddData)
    duUser = np.array(duData)
    uuUser = np.array(uuData)

    distanceDD = distanceCosine(ddOriginalUser, ddUser)
    distanceDU = distanceCosine(duOriginalUser, duUser)
    distanceUU = distanceCosine(uuOriginalUser, uuUser)

    return distanceDU, distanceUU, distanceDD

def treatData(_csv):
    X = []
    x = []
    for row in _csv.iterrows():
        index, data = row
        if index != 0:
            pos = 0
            for value in data:
                if pos != 0:
                    x.append(float(value))
                pos += 1
            X.append(x)
            x = []

    return X

def distanceCosine(vector1, vector2):
    result = 1 - spatial.distance.cosine(vector1, vector2)

    return result

def tranformInformationWCsv(data):
    duData = []
    uuData = []
    ddData = []

    chunkUP = []
    chunkDOWN = []

    if len(data) == 18:
        for x in data:
            if x[2] == "UP":
                chunkUP.append(x)
            if x[2] == "DOWN":
                chunkDOWN.append(x)

        for i in range(9):
            up = chunkUP[i][1]
            down = chunkDOWN[i][1]
            duData.append(int(up) - int(down))

            if i < 8:
                up_1 = chunkUP[i + 1][1]
                down_1 = chunkDOWN[i + 1][1]
                uuData.append(int(up_1) - int(up))
                ddData.append(int(down_1) - int(down))

    return duData, uuData, ddData