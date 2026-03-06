from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import  Contact as ContactModel
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def render_page(request, template_name):
    return render(request, template_name, {'myblog': []})



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = ContactModel(name=name, phone=phone, email=email, message=message)
        contact.save()

        return redirect('contact')  # Redirect to the contact page after saving the message
    
    messages.success(request, "Message sent successfully!")
    return render(request, 'contact.html', {'myblog': []})

