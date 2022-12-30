from django.contrib import messages
from django.http import  HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from core.forms import ContactForm
from core.models import Contacts


class ContactFormView(CreateView):
    model = Contacts
    form_class = ContactForm
    template_name = 'pages/contacts.html'

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            # recipients = ['info@example.com']
            # if cc_myself:
            #     recipients.append(sender)
            #
            # send_mail(subject, message, sender, recipients)
            messages.success(request, 'Thanks for Contacting Us.')
            return render(request, self.template_name, {'form': self.form_class})
        else:
            return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})


class JobsFormView(CreateView):
    model = Contacts
    form_class = ContactForm
    template_name = 'pages/jobs.html'

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            # recipients = ['info@example.com']
            # if cc_myself:
            #     recipients.append(sender)
            #
            # send_mail(subject, message, sender, recipients)]
            messages.success(request, 'Thanks for Contacting Us.')
            return render(request, self.template_name, {'form': self.form_class})
        else:
            return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})