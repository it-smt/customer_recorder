from django.shortcuts import render, redirect

from .forms import RecordForm
from .models import Service, Record, Client, ContactInformation
from users.models import User
from datetime import datetime


def index(request):
    """Функция-представление главной страницы."""
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            contact_information = ContactInformation()
            contact_information.email = cd['email']
            contact_information.phone_number = cd['phone']
            client = Client()
            client.last_name = cd['last_name']
            client.first_name = cd['first_name']
            client.middle_name = cd['middle_name']
            client.contact_info = contact_information
            record = Record()
            datetime_obj = datetime.combine(cd['date'], cd['time'])
            record.date = datetime_obj
            record.service = Service.objects.get(id=cd['pk_service'])
            record.client = client
            record.employee = User.objects.get(id=cd['pk_master'])
            contact_information.save()
            client.save()
            record.save()
            return redirect('main:index')
    else:
        form = RecordForm()
    services = Service.objects.all()
    masters = User.objects.filter(is_master=True)
    context = {
        'services': services,
        'masters': masters,
        'form': form,
    }
    return render(request, 'main/index.html', context=context)
