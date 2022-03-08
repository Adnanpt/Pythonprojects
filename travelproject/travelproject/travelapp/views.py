# Create your views here.
from django.shortcuts import render
from . models import place

def demo(request):
    obj=place.objects.all()
    #name="india"
    return render(request,"index.html",{'result':obj})
    #{'obj':name})
#def about(request):
 #   return render(request,"result.html")
#def addition(request):
  #  x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
  #  res=x+y
  #  return render(request,"result.html",{'result':res})