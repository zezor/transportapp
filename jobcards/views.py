from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import JobCardForm
from .models import JobCard


def create_job_card(request):
    if request.method == 'POST':
        form = JobCardForm(request.POST)
        if form.is_valid():
            job_card = form.save()
            messages.success(
                request,
                f"Job Card {job_card.job_card_no} created successfully!"
            )
            return redirect('job_card_success', job_card_no=job_card.job_card_no)
    else:
        form = JobCardForm()

    return render(request, 'jobcards/create_job_card.html', {'form': form})



def job_card_success(request, job_card_no):
    job_card = get_object_or_404(JobCard, job_card_no=job_card_no)
    return render(
        request,
        'jobcards/job_card_success.html',
        {'job_card': job_card}
    )
    
def job_card_list(request):
    job_cards = JobCard.objects.order_by('-timestamp')
    return render(
        request,
        'jobcards/job_card_list.html',
        {'job_cards': job_cards}
    )
    

def job_card_detail(request, job_card_no):
    job_card = get_object_or_404(JobCard, job_card_no=job_card_no)
    return render(
        request,
        'jobcards/job_card_detail.html',
        {'job_card': job_card}
    )
