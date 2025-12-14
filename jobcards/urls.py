from django.urls import path, include
from . import views


urlpatterns = [ 
    path('create/', views.create_job_card, name='create_job_card'),
    path('detail/<str:job_card_no>/', views.job_card_detail, name='job_card_detail'),
    path('list/', views.job_card_list, name='job_card_list'),
    path('success/<str:job_card_no>/', views.job_card_success, name='job_card_success'),
    path('print/<str:job_card_no>/', views.print_job_card, name='print_job_card'),
]