from django.shortcuts import render
from djanog.http import HttpResponse


# Create your views here.
def main(request):
    return HttpResponse("Howdy")
    
