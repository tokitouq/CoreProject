from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def ost_home_page(request) -> HttpResponse:
    return HttpResponse("It Works")
