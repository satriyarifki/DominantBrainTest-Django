from .models import resulte

fact = []

def rules(fakt):
    tota = 0
    for num in range(10):
        if fakt[num]== 'Ya':
            tota += 1
    toti = 0
    for num in range(11,21):
        if fakt[num]== 'Ya':
            toti += 1
    print(tota)
    print(toti)
    if tota>toti :
        return resulte.objects.get(id=1)
    else :
        return resulte.objects.get(id=2)   
      
               


