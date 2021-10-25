from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def helloworld (request):
 #   return HttpResponse("Hello World")
    
def banco_main_home(request):
    return render(request, 'banco_main_home/home.html')  
