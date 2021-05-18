from django.shortcuts import render


def homepage(request):
    return render(request, "portfolioApp/landing.html")


def aboutpage(request):
    return render(request, "portfolioApp/about.html")
