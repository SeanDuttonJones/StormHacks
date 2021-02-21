from django.shortcuts import render
from django.http import HttpResponse
import csv
import json

# Create your views here.
def maps_page(request):
    company_data = get_company_data()
    company_data_JSON = json.dumps(get_company_data())
    return render(request, "Maps/index.html", {"company_data_JSON": company_data_JSON, "company_data": company_data})

def get_company_data():
    data = []
    with open("Maps/data/company_data.csv", mode='r') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            data.append(row)

    return data