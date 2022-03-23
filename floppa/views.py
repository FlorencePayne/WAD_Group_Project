from django.shortcuts import render
from django.http import HttpResponse
from floppa.forms import NecklaceForm,UserForm, UserProfileForm
from django.shortcuts import redirect
from floppa.forms import UserForm, UserProfileForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
  
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
        
            if user.is_active:
                login(request, user)
                return redirect(reverse('floppa:index'))
            else:
                return HttpResponse("Your Floppabunny account is disabled.")
                
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
            
    else:
        return render(request, 'floppa/login.html')
    
def account(request):
    return render(request, 'floppa/account.html')
      
def signup(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            registered = True
            
        else:
            print(user_form.errors, profile_form.errors)
            
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'floppa/signup.html', context = {'user_form': user_form,
                                                            'profile_form': profile_form,
                                                                'registered': registered})

#can only logout if you're logged in
@login_required
def signout(request):
    logout(request)
    return redirect(reverse('floppa:index'))
    
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