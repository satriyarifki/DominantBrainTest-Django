from django.db import models
from django.shortcuts import render, redirect
from .forms import answerForm, namaTest
from .models import datap, dtest, resulte
from .facts import rules


def index(request):
    namaForm = namaTest(request.POST or None)
    
    if request.method == 'POST':
        if namaForm.is_valid():
            namaForm.save()
            return redirect('ruangtest:testing')
    
    context = {
        'judul' : 'RuangTest',
        'namaForm' : namaForm,
    }
    return render(request, 'test.html', context )

def testing(request):
    testForm = answerForm(request.POST or None)
    datat = datap.objects.all()
    tdata = dtest.objects.all()
    fact = []
    if request.method == 'POST':
        if testForm.is_valid():
            testForm.save()
            fact.append(request.POST.get('ans1')) 
            fact.append(request.POST.get('ans2'))
            fact.append(request.POST.get('ans3'))
            fact.append(request.POST.get('ans4'))
            fact.append(request.POST.get('ans5'))
            fact.append(request.POST.get('ans6'))
            fact.append(request.POST.get('ans7'))
            fact.append(request.POST.get('ans8'))
            fact.append(request.POST.get('ans9'))
            fact.append(request.POST.get('ans10'))
            fact.append(request.POST.get('ans11'))
            fact.append(request.POST.get('ans12'))
            fact.append(request.POST.get('ans13'))
            fact.append(request.POST.get('ans14'))
            fact.append(request.POST.get('ans15'))
            fact.append(request.POST.get('ans16'))
            fact.append(request.POST.get('ans17'))
            fact.append(request.POST.get('ans18'))
            fact.append(request.POST.get('ans19'))
            fact.append(request.POST.get('ans20'))
            fact.append(request.POST.get('ans21'))
            fact.append(request.POST.get('ans22'))
            print(fact)
            tdata = tdata.get(id=request.POST.get('test'))
            dtest.objects.filter(id=request.POST.get('test')).update(hasil=rules(fact))
            print(rules(fact))
            
            
            return render(request, 'result.html', {
                'has' : rules(fact), 'nam' : tdata ,
                'kanan' : resulte.objects.get(id=2),
                'kiri'  : resulte.objects.get(id=1),})
            
    print(fact)
    context = {
        'testForm' : testForm,
        'data' : datat
    }
    
    return render(request, 'testing.html', context)

def result(request):
    dat = dtest.objects.latest('hasil')
    print(dat)
    context = {
        'judul' :'Hasil Test Kamu',
        'dataTest' : dat,
        'kanan' : resulte.objects.get(id=2),
        'kiri'  : resulte.objects.get(id=1),
    }
    return render(request, 'result.html', context)