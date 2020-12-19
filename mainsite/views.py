from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.template import loader


def index(request):
    form = ContactForm()
    context = {'form': form}
    return render(request, 'mainsite/index.html', context)


def send_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['matt_harrop37@hotmail.com']
            if cc_myself:
                recipients.append(sender)
            # send_mail(subject, message, sender, recipients)
    else:
        form = ContactForm()

    context = {'form': form}
    return redirect('index')
