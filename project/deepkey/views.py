from django.shortcuts import render
import csv, random
import pandas as pd
import numpy as np
from scipy import spatial

texts = ['Matéria-prima: Em marcenaria compreende-se por matéria-prima, todo omaterial que entra na confecção dos móveis, tendo por substância essencial amadeira. Definição da madeira. Madeira é uma substância compacta e sólida, quecompõe as raízes, o tronco e as ramas das árvores e dos arbustos. E um conjunto detecidos (parte sólida de um corpo organizado). Seu elemento fundamental é o tecidovascular, constituído de vasos compostos de longas células (pequenas cavidadessobrepostas topo a topo, em filas longitudinais ininterruptas).',
         'Rudimentos de Botânica. A água é o elemento mais necessário à vida vegetal.As raízes, que são órgãos de absorção, sugam da terra o alimento necessário à nutriçãoda planta. A raiz divide-se em três partes: corpo, que é a parte central, prolongamentodo caule; colo ou nó vital, ponto em que o caule se separa da raiz, e as radículas, cujasextremidades, chamadas espongíolos, são os órgãos ativos da absorção.',
         'Caule é a parte da planta que cresce em sentido inverso ao da raiz e quesustenta os galhos, as folhas, as flores e os frutos. Folha é o órgão respiratório dasplantas. Divide-se em duas partes: limbo e pecíolo. No limbo, que é uma lâmina verdee chata, de várias formas, notam-se duas faces, uma superior, mais colorida, e outrainferior; a base, o vértice, a orla. As folhas transpiram pela face superior e absorvem aumidade pela face inferior. Realizam assim as suas duas importantes funções deexalação e absorção. Pecíolo. É assim chamada a parte da folha que prende o limbo aogalho ou ramo. Talo. Chama-se assim a fibra grossa que se estende pelo meio da folha,prolongando-se, às vezes, até confundir-se com o pecíolo.',
         'A música é uma forma de arte que se constitui na combinação de vários sons e ritmos, seguindo uma pré-organização ao longo do tempo. É considerada por diversos autores como uma prática cultural e humana. Não se conhece nenhuma civilização ou agrupamento que não possua manifestações musicais próprias.',
         'O café é uma bebida produzida a partir dos grãos torrados do fruto do cafeeiro. É servido tradicionalmente quente, mas também pode ser consumido gelado. O café é um estimulante, por possuir cafeína — geralmente 80 a 140 mg para cada 207 ml dependendo do método de preparação.']

def modelo1(request):
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

                print(du)
                print(uu)
                print(dd)

                if ddu >= 0.98 and duu >= 0.97 and ddd >= 0.96:
                    return render(request, 'modelo1.html', {'message': 'Bem vindo'})
                else:
                    return render(request, 'modelo1.html', {'error': 'Você não é quem diz ser'})
            else:
                return render(request, 'modelo1.html', {'error': 'Digite a sua senha sem errar'})
        else:
            return render(request, 'modelo1.html', {'error': 'Senha incorreta'})

    return render(request, 'modelo1.html')

def modelo2(request):
    if request.method == 'POST':
        # if not request.POST["data"]:
        #     return render(request, 'modelo2.html', {"false": True, "texto": texts[random.randint(0, 4)]})

        table = brokenData(request.POST["data"], 3)

        # with open('user.csv', 'w') as csv_file:
        #     writer = csv.writer(csv_file)
        #     writer.writerows(table)
        #
        # if (compareModel2(moreData())):
        #     return render(request, 'modelo2.html', {"true": True, "texto": texts[random.randint(0, 4)]})
        # else:
        #     return render(request, 'modelo2.html', {"false": True, "texto": texts[random.randint(0, 4)]})

        with open('table2Modelo2.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(table)
    # moreData()

    return render(request, 'modelo2.html', {"texto": texts[random.randint(0, 4)]})

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

def vectorizeDynamicData():

    # path to dataframe file
    DF_FILE = ''

    # time that breaks timeseries
    TIME_TRSHLD = 1.2

    input_df = pd.read_csv(DF_FILE,header = None)

    # list that contains stops in dynamic types
    breaks=[]

    for idx in input_df.index:
        if not idx < len(input_df):
            break               # breaks when it is done

        atsp = input_df[1].iloc[idx] # actual timestamp
        ntsp = input_df[1].iloc[idx+1] # next timestamp

        dist = ntsp - atsp       # distance between

        if dist > TIME_TRSHLD:  # if difference between typing is greater then threshold
            breaks.append(ntsp)

    # three types of data
    small = []
    medium = []
    large = []

    # separates the chunks of data into 3 groups
    for i in range(len(breaks)):
        if not i < len(breaks):
            break

        actual = breaks[i]      # start of time series
        next = breaks[i+1]      # end of time series

        diff = next - actual    # difference between all keyboard events (down & up)
        if diff < 30:
            small.append(actual)

        elif diff < 60:
            medium.append(actual)

        elif diff < 90:
            large.append(actual)

def moreData():
    df = pd.read_csv('tableModelo2.csv', header=None)

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

    chunkDOWN = []

    for first in lData:
        for second in first:
            if second[2] == "DOWN":
                chunkDOWN.append(second)

    mini = []
    dd = []
    for i in chunkDOWN:
        mini.append(i)
        if (len(mini) == 2):
            dd.append(mini[1][1] - mini[0][1])
            mini = []
            mini.append(i)

    ba = []
    chunks = []

    for i, value in enumerate(dd):
        ba.append(value)
        if (i + 1) % 30 == 0:
            chunks.append(ba)
            ba = []

    return chunks

    # chunks = []
    # mChunk = []
    # for data in dd:
    #     if data >= 1000 and data <= 2000:
    #         chunks.append(mChunk)
    #         mChunk = []
    #     mChunk.append(data)
    #
    # chunks.append(mChunk)

def compareModel2(my_chunks):
    df = pd.read_csv('user.csv', header=None)

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

    chunkDOWN = []

    for first in lData:
        for second in first:
            if second[2] == "DOWN":
                chunkDOWN.append(second)

    mini = []
    dd = []
    for i in chunkDOWN:
        mini.append(i)
        if (len(mini) == 2):
            dd.append(mini[1][1] - mini[0][1])
            mini = []
            mini.append(i)

    ba = []
    chunks = []

    for i, value in enumerate(dd):
        ba.append(value)
        if (i + 1) % 30 == 0:
            chunks.append(ba)
            ba = []

    if len(chunks) == 0:
        return False

    ok = 0
    for my_chunk in my_chunks:
        for i in range(len(chunks)):
            print(distanceCosine(my_chunk, chunks[i]))
            if (distanceCosine(my_chunk, chunks[i]) >= 0.70):
                ok += 1
        print()

    print(str(ok) + " de " + str(len(my_chunks) * len(chunks)))

    if (ok >= (len(my_chunks) * len(chunks)) / 2):
        return True
    else:
        return False