from django.urls import path

from portfolioApp.views import homepage, aboutpage

urlpatterns = [
    path('', homepage, name='home'),
    path('about/', aboutpage, name='about')
]
