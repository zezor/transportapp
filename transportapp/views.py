from django.shortcuts import render

def home(request):
    return render(request, 'jobcards/home.html')


def dashboard(request):
    return render(request, 'jobcards/dashboard.html')
