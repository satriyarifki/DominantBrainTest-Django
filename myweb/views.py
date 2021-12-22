from django.shortcuts import render

def index(request):
    context = {
        'judul' : 'Test Kepribadian'
    }
    return render(request, 'index.html', context)

