from django.shortcuts import render
from .password_change import password_change
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomLoginForm


### Custom Login & Logout View ###

class CustomLoginView(LoginView):
    template_name = 'app/users/login.html'
    authentication_form = CustomLoginForm

    def get_success_url(self):
        return reverse_lazy('home')  # Redirect after login

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Redirect if already logged in
        return super().dispatch(request, *args, **kwargs)


def custom_logout(request):
    logout(request)
    return redirect('login')

### End Custom Login & Logout View ###