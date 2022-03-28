from django.shortcuts import render
from django.http import HttpResponse
from floppa.forms import NecklaceForm,UserForm, UserProfileForm
from django.shortcuts import redirect
from floppa.forms import UserForm, UserProfileForm, AddToCartForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from floppa.models import Necklace, Order, Order_Necklace, Customer
from django.shortcuts import render

# create view with request as parameter which also returns the context dictionary 
def index(request):
    context_dict = {'boldmessage': 'Necklaces'}
    return render(request, 'floppa/index.html', context=context_dict)

def about(request):
    return render(request, 'floppa/about.html')

def contact(request):
    return render(request, 'floppa/contact.html')
     
def signin(request):
    # retrive input from the user and create user vairable with inputs
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        #if statement to handle different instances of user being logged in
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
    customers = Customer.objects.get(user_id = request.user.id)
    return render(request, 'floppa/account.html', context={'customers':customers})
      
def signup(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        # if statement to check if the sign up form is valid and to register the user
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
    necklaces = Necklace.objects.all()
    context_dict = {"necklaces":necklaces}
    return render(request, 'floppa/necklaces.html', context=context_dict)

def necklace(request, necklace_name_slug):
    context_dict = {}
    form = AddToCartForm()

    try:
        necklace = Necklace.objects.get(slug=necklace_name_slug)
        context_dict['necklace'] = necklace
        upper = necklace.name.upper()
        context_dict['upper'] = upper
    except Necklace.DoesNotExist:
        context_dict['necklace'] = None
        context_dict['upper'] = None
        
    if request.method == "POST":
        if request.user.is_authenticated:
            form = AddToCartForm(request.POST)
            
        if form.is_valid():
            cart = form.save(commit=False)
            customer = Customer.objects.get(user_id = request.user.id)
            cart = Order.objects.get_or_create(userID = customer)[0]
            cart.orderID_id = cart.id
            
            cartNecklace = Order_Necklace.objects.get_or_create(orderID_id = cart.orderID_id, necklaceID_id = necklace.id)[0]
            cartNecklace.necklaceID_id = necklace.id
            cartNecklace.quantity = form.cleaned_data['quantity']
            
            if cartNecklace.quantity == 0:
                cartNecklace.delete()
                cart.save()
            else:    
                cart.save()
                cartNecklace.save()
            
        else:
            print(form.errors)
    
    context_dict['form'] = form
    return render(request, 'floppa/necklace.html', context=context_dict)    


def add_necklace(request):
    form = NecklaceForm()
    
    if request.method == 'POST':
        form = NecklaceForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return redirect('floppa:necklaces')
        else:
            print(form.errors)
            
    return render(request, 'floppa/add_necklace.html', {'form': form})        


def cart(request):
    context_dict = {}
    necklacesDict = []
    prices = []
    records = []
    counter = 0;
    
    customer = Customer.objects.get(user_id = request.user.id)
    cart = Order.objects.get_or_create(userID_id = customer.user_id)[0]
    cart.orderID_id = cart.id
    necklaces = Order_Necklace.objects.filter(orderID_id = cart.orderID_id)
    
    for necklaceRef in necklaces:
        necklace = Necklace.objects.get(id = necklaceRef.necklaceID_id)
        price = int(necklace.price.replace('£', '')) * int(necklaceRef.quantity)
        
        necklacesDict.append(necklace)
        prices.append(price)
        records.append(counter)
        counter += 1
    
    context_dict['necklaces'] = necklacesDict
    context_dict['prices'] = prices
    context_dict['records'] = records
    return render(request, 'floppa/cart.html', context=context_dict)
 
def checkout(request):
    total = 0
    context_dict = {}
    
    customer = Customer.objects.get(user_id = request.user.id)
    cart = Order.objects.get_or_create(userID_id = customer.user_id)[0]
    cart.orderID_id = cart.id
    necklaces = Order_Necklace.objects.filter(orderID_id = cart.orderID_id)
    
    for necklaceRef in necklaces:
        necklace = Necklace.objects.get(id = necklaceRef.necklaceID_id)
        price = int(necklace.price.replace('£', '')) * int(necklaceRef.quantity)
        total += price
        
    context_dict['total'] = total    
    return render(request, 'floppa/checkout.html', context=context_dict)
 
def payment_confirmed(request):
    return render(request, 'floppa/paymentConfirmed.html')