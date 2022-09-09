from django.shortcuts import render, HttpResponse

# from multiprocessing import context
# from django.contrib import messages
# from datetime import datetime
# from gokuportfolio.models import Contact


# Create your views here.


def home(request):
    # if request.method == "POST":
    # fullname = request.POST.get('fullname')
    # email = request.POST.get('email')
    # phone = request.POST.get('phone')
    # message = request.POST.get('message')
    # contact = Contact(fullname=fullname, email=email, phone=phone, message=message, date=datetime.today())
    # contact.save()
    # messages.success(request, 'Your message has been sent')
    return render(request, 'home.html')