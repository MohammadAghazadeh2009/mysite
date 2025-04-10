from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from website.forms import ContactForm, NewsLetterForm
from django.contrib import messages

def home(request):
    return render(request, "website/index.html")

def about(request):
    return render(request, "website/about.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            change = form.save(commit=False)
            change.name = 'unknown'
            change.save()
            messages.add_message(request, messages.SUCCESS, 'your message sent successfully')
        else:
            messages.add_message(request, messages.ERROR, 'something went wrong')

    form = ContactForm()
    return render(request, "website/contact.html",{'form':form})


def newsletter(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        return HttpResponseRedirect('/')
         