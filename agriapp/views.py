from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect # redirect to direct url redirect(to)
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .forms import ContactForm, DeviseForm
from .models import ContactDetails, Devise


# Create your views here.

def home(request):
    if request.method == 'GET':
        template_name = 'home1.html'
        return render(request, template_name)
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'home1.html', {'errors': form.errors})
        
        template_name = 'home1.html'
        return render(request, template_name)

def login(request):
    context = dict()
    if request.method == 'GET':
        template_name = 'login1.html'
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            # template_name = '/map/map_index.html'
            return redirect('/map/')
        else:
            template_name = 'login1.html'
            context       =  {'error' : 'Invalid username or password'}
    return render(request, template_name, context = context)
    
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='/')    
def users(request):
    template_name = "users.html"
    return render(request, template_name)

@login_required(login_url='/')    
def add_devise(request):
    context = {'message' : ''}
    if request.method == 'GET':
        template_name = "add_devise.html"
    elif request.method == 'POST':
        form = DeviseForm(request.POST)
        if form.is_valid():
            form.save()
            template_name = 'map/map_index.html'
            context = {'message' : 'Devise added successfully'}
        else:
            print(form.errors['amount_paid'])
            return render(request, 'add_devise.html', {'errors': form.errors})
    return render(request, template_name = template_name,)

@login_required(login_url='/')    
def notifications(request, **kwargs):
    if (kwargs):
       data = ContactDetails.objects.get(pk = kwargs['pk'])
       data.status = False
       data.save()
    
    notifications_all = ContactDetails.objects.all()
    template_name     = 'notifications.html'
    context = {
        'notification_active'   : notifications_all.filter(status=True),
        'notification_inactive' : notifications_all.filter(status=False),
    }
    return render(request, template_name = template_name, context = context)

@login_required(login_url='/')    
def devise_list(request, **kwargs):
    devises = Devise.objects.all()
    template_name     = 'device_list.html'
    
    context = {
        'devise_count' :len(devises),
        'devises'      : devises,
    }
    return render(request, template_name = template_name, context = context)
