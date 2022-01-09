from django.shortcuts import render

# Create your views here.

def profile(request):
    template = 'profiles/profiles.html'
    context = {

    }

    return render(request, template, context)