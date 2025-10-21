from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')

def terms_conditions(request):
    return render(request, 'core/terms_conditions.html')
