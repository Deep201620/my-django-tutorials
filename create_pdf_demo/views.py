from django.shortcuts import render
from reportlab.pdfgen import canvas
from django.http import HttpResponse

# Create your views here.


def getpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 50)
    p.setTitle("Demo PDF creating using Python ReportLab library")
    p.setAuthor("Deep")
    p.drawString(100, 700, "Hello From Deep Shah")
    p.showPage()
    p.save()
    return response