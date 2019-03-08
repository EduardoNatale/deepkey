from django.shortcuts import render
import csv

def deepkey(request):
    if request.method == 'POST':
        if request.POST.get('input-password', None) == 'qwerty123':
            table1 = brokenData(request.POST.get('inputTable1', None), 3)
            table2 = brokenData(request.POST.get('inputTable2', None), 3)
            table3 = brokenData(request.POST.get('inputTable3', None), 3)

            with open('tabela1.csv', 'a') as csv1:
                writer = csv.writer(csv1)
                writer.writerows(table1)
            with open('tabela2.csv', 'a') as csv2:
                writer = csv.writer(csv2)
                writer.writerows(table2)
            with open('tabela3.csv', 'a') as csv3:
                writer = csv.writer(csv3)
                writer.writerows(table3)

        return render(request, 'index.html')
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
