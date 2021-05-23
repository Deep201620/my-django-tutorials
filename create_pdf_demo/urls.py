from django.urls import path
from create_pdf_demo import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pdf/',views.getpdf)

]