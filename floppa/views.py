from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
def index(request):
    context_dict = {'boldmessage': 'Necklaces'}
    return render(request, 'floppa/index.html', context = context_dict)

def about(request):
    return render(request, 'floppa/about.html')
