from django.shortcuts import render

# Create your views here.
def set(request):
    data=render(request,'set.html')
    data.set_cookie('name', 'himanshi')
    data.set_cookie('age', '21',max_age=3*24*60*60,secure=True,httponly=True)
    data.set_cookie('city', 'Bhopal')
    return data

def get(request):
    print(request.COOKIES)
    nm=request.COOKIES['name']
    ag=request.COOKIES['age']
    ct=request.COOKIES['city']
    data={
        'name':nm,
        'age':ag,
        'city':ct
    }
    return render(request,'get.html',data)



