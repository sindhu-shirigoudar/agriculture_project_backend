from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect # redirect to direct url redirect(to)
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .forms import ContactForm, DeviseForm
from .models import ContactDetails, Devise

from . import UserFuncrtions


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
            UserFuncrtions.create_user(request.POST['devise_id'], request.POST['email'])
            form.save()
            template_name = 'dsahboard.html'
            context = {'message' : 'Devise added successfully'}
        else:
            errors  = form.errors
            field_errors = dict()
            for error in errors:
                field_errors[error] = errors[error]

            default_values = {
                'name'           : request.POST['name'],
                'devise_id'      : request.POST['devise_id'],
                'setial_no'      : request.POST['setial_no'],
                'chipset_no'     : request.POST['chipset_no'],
                'email'          : request.POST['email'],
                'address1'       : request.POST['address1'],
                'address2'       : request.POST['address2'],
                'purchase_date'  : request.POST['purchase_date'],
                'time_of_sale'   : request.POST['time_of_sale'],
                'warrenty'       : request.POST['warrenty'],
                'amount_paid'    : request.POST['amount_paid'],
                'balance_amount' : request.POST['balance_amount'],
                'phone'          : request.POST['phone'],
            }
            return render(request, 'add_devise.html', {'devise' : default_values, 'field_errors' : field_errors})
    return render(request, template_name = template_name,)

@login_required(login_url='/')    
def edit_devise(request, **kwargs):
    context = {'message' : ''}
    devise  = Devise.objects.get(pk = kwargs['pk'])
    print(devise.time_of_sale,devise.purchase_date,'-----')
    if request.method == 'GET':
        template_name = "add_devise.html"
        context       = {
            'devise' : devise,
        }
    elif request.method == 'POST':
        form = DeviseForm(request.POST or None, instance=devise)
        if form.is_valid():
            form.save()
            template_name = 'dashboard.html'
            context = {'message' : 'Devise updated successfully'}
        else:
            print(request.POST)
            return render(request, 'add_devise.html', {'errors': form.errors, 'devise' : devise, })
    return render(request, template_name = template_name, context=context)

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

@login_required(login_url='/')    
def devise_details(request, **kwargs):
    devise  = Devise.objects.get(pk = kwargs['pk'])
    template_name = "devise_details1.html"
    context       = {
        'devise' : devise,
    }
    return render(request, template_name = template_name, context=context)
