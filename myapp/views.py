from django.shortcuts import render
from . models import datas
# Create your views here.
def homes(request):
    pro=datas.objects.all()
    return render(request,'homes.html',{'pr':pro})
