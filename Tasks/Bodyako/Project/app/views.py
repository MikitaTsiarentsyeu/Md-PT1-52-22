from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.views.generic import View


# Create your views here.

def home(request):
    return render(request, 'home.html')

class FeedbackView(View):
    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/#popup6')

    
