from django.views.generic import CreateView
# from .models import User
from .forms import SignupForm
from django.urls import reverse_lazy

class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('accounts:login')





