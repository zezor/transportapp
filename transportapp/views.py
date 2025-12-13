from django.shortcuts import render

def home(request):
    return render(request, 'jobcards/home.html')

def create_job_card(request):
    
    return render(request, 'jobcards/create_job_card.html')

def dashboard(request):
    return render(request, 'jobcards/dashboard.html')
