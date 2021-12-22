from django.urls import path, re_path


from . import views

app_name= 'ruangtest'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^testing/$', views.testing, name='testing'),
    re_path(r'^result/$', views.result, name='result'),
    
]
