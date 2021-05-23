from django.urls import path
from email_app import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mail/', views.mail)
]