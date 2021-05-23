from django.urls import path
from CSV_lib_demo import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('csv/',views.getfile)

]