from django.contrib import admin
from mysite import views
from django.urls import path, include

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('mysite/', views.index),
    path('mysite/chart2/',views.chart),
    path('mysite/our/',views.our),
    path('mysite/datasum/',views.datasum),
]
