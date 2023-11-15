from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from mysite import models
from mysite import filter
import random
import os
 
def index(request):
    alldata = models.alldata.objects.all()
    end = models.enddate.objects.all()
    
    alldataFilter = filter.alldataFilter(queryset=alldata)
    
    if request.method == "POST":
        alldataFilter = filter.alldataFilter(request.POST, queryset=alldata)
 
    context = {
        'alldataFilter': alldataFilter,
        'enddate': end
    }
 
    return render(request, 'mysite/index.html', context)


def chart(request):
    alldata = models.alldata.objects.all()
    end = models.enddate.objects.all()
    alldataFilter = filter.alldataFilter(queryset=alldata)
 
    if request.method == "POST":
        alldataFilter = filter.alldataFilter(request.POST, queryset=alldata)
 
    context = {
        'alldataFilter': alldataFilter,
        'enddate': end
    }
 
    return render(request, 'mysite/chart2.html', context)

def our(request):
    end = models.enddate.objects.all()
    context = {
        'enddate': end
    }
    return render(request, 'mysite/our.html', context)


def datasum(request):
    alldata = models.alldata.objects.all()
    end = models.enddate.objects.all()
    alldataFilter = filter.alldataFilter(queryset=alldata)
 
    if request.method == "POST":
        alldataFilter = filter.alldataFilter(request.POST, queryset=alldata)
 
    context = {
        'alldataFilter': alldataFilter,
        'enddate': end
    }
    return render(request, 'mysite/datasum.html', context)