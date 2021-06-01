from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('values', views.values, name='values'),
    path('about',views.about, name='about'),
    path('confirm',views.confirm, name='confirm')
]

