import requests

from django.shortcuts import render, HttpResponse
from requests.api import get
from .models import Contact
from .send_email import sendEmail

# Create your views here.
def get_data(endpoint):
    response = requests.get(endpoint)
    return response.json()


def index(request):
    return render(request, 'home/index.html', {
        'courses': get_data('https://api.npoint.io/53897478e13604a83e77'),
        'yt_videos': get_data('https://api.npoint.io/1e3ad07b9c9b7fcf4f20'),
        'developers': get_data('https://api.npoint.io/952ccba723fbe7772407')
    })


def about(request):
    return HttpResponse("This is about page")


def courses(request):
    return HttpResponse("This is courses page")


def contact(request):
    info_dict = {
        'message': 'Have any Queries ? <br> Have some suggestion or idea to share ?'
    }

    if request.method == "POST":
        # fetch data from html Raw form
        name = request.POST.get("name")
        phNo = request.POST.get("ph_No")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to DB
        new_contact = Contact(name=name, email=email,
                              phone_number=phNo, message=message)
        new_contact.save()

        # Send mail
        send_mail = sendEmail(user_name=name, user_email=email,
                              user_phone=phNo, user_msg=message)
        send_mail.send()
        info_dict['message'] = f'Thanks {name} for share your thoughts, <br> we\'ll contact with you soon.'

    return render(request, 'home/contact.html', info_dict)
