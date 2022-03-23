from django.shortcuts import render
from django.http import HttpResponse
from floppa.forms import NecklaceForm
from django.shortcuts import redirect

from django.shortcuts import render
def index(request):
    context_dict = {'boldmessage': 'Necklaces'}
    return render(request, 'floppa/index.html', context=context_dict)

def about(request):
    return render(request, 'floppa/about.html')
    
def cart(request):
    return render(request, 'floppa/cart.html')
    
def checkout(request):
    return render(request, 'floppa/checkout.html')
  
def login(request):
    return render(request, 'floppa/login.html')
    
def account(request):
    return render(request, 'floppa/account.html')
      
def signup(request):
    return render(request, 'floppa/signup.html')
    
def necklaces(request):
    return render(request, 'floppa/necklaces.html')
    
def add_necklace(request):
    form = NecklaceForm()
    
    if request.method == 'POST':
        form = NecklaceForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return redirect('/floppa/necklaces')
        else:
            print(form.errors)
    return render(request, 'floppa/add_necklace.html', {'form': form})        