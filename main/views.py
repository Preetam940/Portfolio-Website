from django.shortcuts import render


def home(req):
    return render(req, 'main/Home.html')


def projects(req):
    return render(req, 'main/Projects.html')


def contact(req):
    return render(req, 'main/contact.html')
