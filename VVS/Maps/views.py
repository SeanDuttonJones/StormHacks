from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def maps_page(request):
    # mapHTML = "Maps/index.html"
    # return render(request, mapHTML)
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, "Maps/index.html")

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)