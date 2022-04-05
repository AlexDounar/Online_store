from django.shortcuts import render


def home(request):
    return render(request, 'online_store/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'online_store/about.html', {'title': 'About'})


def contacts(request):
    return render(request, 'online_store/contacts.html', {'title': 'Contact us'})


def catalogue(request):
    return render(request, 'online_store/catalogue.html', {'title': 'Catalogue'})


def login(request):
    return render(request, 'online_store/login.html', {'title': 'Login'})


def search(request):
    return render(request, 'online_store/search.html', {'title': 'Search'})


def delivery(request):
    return render(request, 'online_store/delivery.html', {'title': 'Delivery'})

