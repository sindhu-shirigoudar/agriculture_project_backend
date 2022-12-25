from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect # redirect to direct url redirect(to)
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .forms import ContactForm, DeviseForm
from .models import ContactDetails, Devise, DeviseApis

from . import UserFuncrtions
from django.views.generic import UpdateView
from django.urls import reverse
from django.contrib import messages #import messages
from datetime import datetime

# Create your views here.

def home(request):
    if request.method == 'GET':
        template_name = 'home1.html'
        return render(request, template_name)
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Contact details added successfully")
        else:
            return render(request, 'home1.html', {'errors': form.errors})
        
        template_name = 'home1.html'
        return render(request, template_name, {'message' : 'Contact details has been added successfully'})

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
            return redirect('/dsahboard/')
        else:
            template_name = 'login1.html'
            context       =  {'error' : 'Invalid username or password'}
    return render(request, template_name, context = context)
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def users(request):
    template_name = "users.html"
    return render(request, template_name)

def add_devise(request):
    context = {'message' : ''}
    if request.method == 'GET':
        template_name = "add_devise.html"
    elif request.method == 'POST':
        form = DeviseForm(request.POST)
        if form.is_valid():
            UserFuncrtions.create_user(request.POST['devise_id'], request.POST['email'])
            form.save()
            template_name = 'device_list.html'
            messages.success(request,"Devise added successfully")
            return redirect("/device-list/")
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
    return render(request, template_name = template_name, context=context)

def edit_devise(request, **kwargs):
    context = {'message' : ''}
    devise  = Devise.objects.get(pk = kwargs['pk'])
    devise.purchase_date = datetime.strptime(str(devise.purchase_date), '%Y-%m-%d')
    devise.warrenty = datetime.strptime(str(devise.warrenty), '%Y-%m-%d')
    if request.method == 'GET':
        template_name = "add_devise.html"
        context       = {
            'devise' : devise,
        }
    elif request.method == 'POST':
        form = DeviseForm(request.POST or None, instance=devise)
        if form.is_valid():
            form.save()
            messages.success(request,"Devise updated successfully")
            return redirect("/device-list/")
        else:
            print(request.POST)
            return render(request, 'add_devise.html', {'errors': form.errors, 'devise' : devise, })
    return render(request, template_name = template_name, context=context)

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

def devise_list(request, **kwargs):
    if request.method == 'POST':
        pk = request.POST['pk']
        if pk:
            devises = Devise.objects.filter(pk=request.POST['pk'])
        else :
            devises = Devise.objects.all()
    else:
        devises = Devise.objects.all()

    devices = Devise.objects.all()
    template_name     = 'device_list.html'
    
    context = {
        'devise_count' :len(devises),
        'devises'      : devises,
        'devices'      : devices,
    }
    return render(request, template_name = template_name, context = context)

def api_list(request, **kwargs):
    devise = Devise.objects.get(pk = kwargs['pk'])
    apis = DeviseApis.objects.filter(device__pk=kwargs['pk'])
    template_name     = 'api_list.html'
    context = {
        'api_count'   : len(apis),
        'apis'        : apis,
        'devise' : devise,
    }
    return render(request, template_name = template_name, context = context)

def devise_details(request, **kwargs):
    devise  = Devise.objects.get(pk = kwargs['pk'])
    apis    = DeviseApis.objects.filter(device=devise)
    template_name = "devise_details1.html"
    context       = {
        'devise' : devise,
        'api_usage' : len(apis),
    }
    return render(request, template_name = template_name, context=context)

def api_overview(request, **kwargs):
    api = DeviseApis.objects.get(pk=kwargs['pk'])
    template_name = "api_details.html"
    context = {
        'api' : api,
        'devise_name' : api.device.name,
    }
    return render(request, template_name = template_name, context=context)

class UpdateApi(UpdateView):
    model = DeviseApis
    fields = '__all__'
    template_name = 'updaet-api.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateApi, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        messages.success(self.request, "API updated successfully")
        return context

    def get_success_url(self):
        return reverse('api-overview', kwargs={'pk': self.kwargs['pk']})