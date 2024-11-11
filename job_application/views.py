from django.shortcuts import render
from .forms import ApplicationForms
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

"""def index(request):
    if request.method == 'POST':
        form = ApplicationForms(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']
            print(form)
    return render(request, 'index.html')"""


def index(request):
    print("View function called")
    if request.method == 'POST':
        print("POST request received")
        form = ApplicationForms(request.POST)
        print("Form instantiated")
        if form.is_valid():
            print("Form is valid")
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']
            Form.objects.create(first_name=first_name, last_name=last_name,
                                emails=email, date=date, occupation=occupation)
            message_body = f'Your application submitted. Thanks {first_name}'
            email_message = EmailMessage('Job Application submitted',
                                 message_body, to=[email])
            email_message.send()
            messages.success(request, 'Form Submitted Successfully!')
            print("Form data:", first_name, last_name, email, date, occupation)
    return render(request, 'index.html')
