from django.shortcuts import render


def home(request):
    """Render the home page with personal information"""
    return render(request, 'resume/home.html', {})
