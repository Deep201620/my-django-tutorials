from django.urls import path
from session_demo import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/',views.setsession),
    path('get/', views.getsession),
    path('setck/', views.setcookies),
    path('getck/', views.getcookies)
]