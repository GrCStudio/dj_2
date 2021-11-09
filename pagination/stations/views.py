import csv
from urllib.parse import urlencode
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    stations = []
    with open('data-398-2018-08-30.csv', encoding='utf8', newline='') as importfile:
        filereader = csv.DictReader(importfile)
        for row in filereader:
            stations.append(row)
    paginator = Paginator(stations, 10)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)

    return render(request, 'stations/index.html', context={
        'bus_stations': page.object_list,
        'page': page
    })

