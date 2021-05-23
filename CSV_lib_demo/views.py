from django.shortcuts import render
import csv
from django.http import HttpResponse
# Create your views here.

def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['content-Disposition'] = 'attachment; filename="file.csv"'
    writer = csv.writer(response)
    # writer.writerow(['1001', 'John', 'Deep', 'CA'])
    # writer.writerow()
    params =[ ['1001', 'John', 'Deep', 'CA'],['1002','Aayush','Toyota','Switzerland'],['1004', 'Sunil', 'Accenture', 'Pune']]
    writer.writerows( params)
    return response