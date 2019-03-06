from django.shortcuts import render

def deepkey(request):
    if request.method == 'POST':
        pass
    return render(request, 'index.html')
