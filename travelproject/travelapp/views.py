# Create your views here.
from django.shortcuts import render

from travelapp.models import place, place1


def demo(request):
    obj=place.objects.all()
    #name="india"
    return render(request,"index.html",{'result':obj})

# def demo1(request):
#     obj = place1.objects.all()
#     # name="india"
#     return render(request, "index.html", {'result1': obj})

    #{'obj':name})
#def about(request):
 #   return render(request,"result.html")
#def addition(request):
  #  x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
  #  res=x+y
  #  return render(request,"result.html",{'result':res})