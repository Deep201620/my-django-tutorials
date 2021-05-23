from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from Django_tutorials import settings
# Create your views here.


def mail(request):
    subject = "Greetings"
    msg = "Congratulations for your Success"
    to = "deep19731@gmail.com"
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if res == 1:
        msg = "Mail sent successfully"
    else:
        msg = "Mail could not sent"
    return HttpResponse(msg)