from django import forms
from django.contrib.postgres.fields import ArrayField
from django.db.models import fields
from django.db.models.base import Model
from django.forms import widgets
from django.forms.models import ALL_FIELDS

from .models import answer, dtest

class namaTest(forms.ModelForm):
    class Meta :
        model = dtest
        fields = {
            'nama',
        }
        
        labels = {
            'nama' : 'Nama Peserta '
        }
        
        widgets = {
            'nama' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'type'  : 'text',
                    'placeholder' : 'Masukkan Nama ..',
                    'id' : 'exnama',
                    
                }
                
            )
        }

class answerForm(forms.ModelForm):
    class Meta :
        model = answer
        fields=[
            'test',
            'ans1',
            'ans2',
            'ans3',
            'ans4',
            'ans5',
            'ans6',
            'ans7',
            'ans8',
            'ans9',
            'ans10',
            'ans11',
            'ans12',
            'ans13',
            'ans14',
            'ans15',
            'ans16',
            'ans17',
            'ans18',
            'ans19',
            'ans20',
            'ans21',
            'ans22'
        ]
        
        labels = {
            'test' : "Nama Peserta",
            'ans1' : 'Saya dapat berpikir secara berurutan, mampu mengingat penjelasan,dan mengingat detail',
            'ans2' : 'Saya mampu menghasilkan sesuatu dengan matang dan terstruktur',
            'ans3' : 'Bagi saya, prestasi akademik (ranking dan nilai IPK) adalah hal yangpenting dan harus diperjuangkan',
            'ans4' : 'Saya mampu berpikir analitis, berdasarkan fakta, tajam, dan jelas',
            'ans5' : 'Saya melakukan pekerjaan dengan serius dan cermat',
            'ans6' : 'Saya sering membuat rencana dan perhitungan matang sebelummelakukan sesuatu',
            'ans7' : 'Saya suka kedisiplinan dan terkadang membuat peraturan untuk dirisendiri',
            'ans8' : 'Saya menghafal dengan baik dalam kata-kata dan penjelasan',
            'ans9' : 'Saya agak tertutup dan kurang suka berinteraksi dengan orang lain',
            'ans10': 'Saya menyukai sesuatu yang teratur, terpola, dan baku', 
            'ans11': 'Saya menyukai angka, hitungan, dan sesuatu yang berhubungandengan logika',
            'ans12': 'Mampu mencari jalan keluar dengan cara yang baru dan mencari idekreatif',
            'ans13': 'Tertarik belajar sesuatu hal yang baru dan unik',
            'ans14': 'Menyukai warna, gambar, dan musik',
            'ans15': 'Suka berkhayal dan berimajinasi',
            'ans16': 'Mampu menyesuaikan diri dengan lingkungan baru',
            'ans17': 'Enterpreneur yang sukses meskipun tidak sekolah tinggi',
            'ans18': 'Bersifat terbuka, suka bergaul dengan semua orang, humoris, dan lucu',
            'ans19': 'Menyukai petualangan, tantangan, suka kebebasan, dan tidak mauterikat',
            'ans20': 'Tidak suka pada rumus, hitungan, dan logika yang terlalu banyak',
            'ans21': 'Dapat berpikir secara tidak berurutan, kreatif, dan menyebar',
            'ans22': 'Suka melakukan pekerjaan dengan cara sendiri dan membuat cara baruyang nyaman',
        }
        widgets = {
            'test' : forms.Select(
                attrs = {
                    'class' : 'mb-5',
                    'type'  : 'text',
                    'placeholder' : 'Masukkan Nama ..',
                    'id' : 'exnama',
                    
                }
                
            )
        }
        


