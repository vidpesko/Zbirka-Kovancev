from django.shortcuts import render
from .models import Topic
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    # TOPICS
    topics = Topic.objects.all()

    # NUMBERS
    num_of_users = len(User.objects.all())
    average_size = 12
    biggest_collection = 30
    all_collected = 100
    statistics = {
        'users':num_of_users,
        'average_size': average_size,
        'biggest_collection': biggest_collection,
        'all_collected':all_collected,
    }

    context = {'topics':topics, 'stats':statistics}
    return render(request, 'home/Domov.html', context)
