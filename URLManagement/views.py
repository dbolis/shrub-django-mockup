from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def landing(request):
    return render(request,'landing.html')

def values(request):
    return render(request,'values.html')

def about(request):
    return render(request,'about.html')

def confirm(request):
    price=request.POST.get("price",False)
    quote = (int(price.replace(",","")))//50
    if price==False:
        return render(request,'landing.html')
    else:
        return render(request, 'confirm.html',{"price":price, "quote":quote})