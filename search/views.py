from django.shortcuts import render

# Create your views here.
def search(request, q=None):

    context = {}
    return render(request, 'search/Razisci.html', context)
