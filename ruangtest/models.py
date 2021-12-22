
from django.db import models
from django.forms.utils import ErrorDict, ErrorList

class yrn(models.Model):
    code = models.CharField(max_length=5)
    yrn = models.CharField(max_length=100)
    

class resulte(models.Model):
    code = models.CharField(max_length=5)
    tipe = models.CharField(max_length=100)
    
    def __str__(self):
        ownself = '{0.tipe}'
        return ownself.format(self)
    
    
class dtest(models.Model):
    nama = models.CharField(max_length=30)
    hasil = models.ForeignKey(resulte, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        ownself = '{0.nama}'
        return ownself.format(self)
    
class datap(models.Model):
    code = models.CharField(max_length=5)
    indikator = models.CharField(max_length=100)
    
    def __str__(self):
        ownself = '{0.code} {0.indikator}'
        return ownself.format(self)

class answer(models.Model):
    test = models.ForeignKey(dtest, on_delete=models.CASCADE, null=True, blank=True)
    List_answer = (
        ('Ya', 'ya'),
        ('Tidak', 'tidak'),
    )
    ans1 = models.CharField(
        max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans2 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        blank=True,
        null=True)
    ans3 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans4 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans5 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans6 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans7 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans8 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans9 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans10 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans11 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans12 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans13 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans14 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans15 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans16 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans17 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans18 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans19 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans20 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans21 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    ans22 = models.CharField( max_length= 10,
        choices= List_answer,
        default= '',
        null=True, blank=True)
    
    def __str__(self):
        ownself = '{0.test}'
        return ownself.format(self)