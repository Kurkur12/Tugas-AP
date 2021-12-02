from django.shortcuts import render
from django.http import HttpResponse

import time

def coba(request):
    now = time.ctime()
    tm = "<html><body><h1>My name is <i>{nama}</i></h1><h2>It is now {waktu}<h2><hr></body></html>"
    hasil = tm.format(nama = "Kurniawan Bagaskara", waktu = now)
    return HttpResponse(hasil)
# Create your views here.
