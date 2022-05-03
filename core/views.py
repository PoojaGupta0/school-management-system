from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

User = get_user_model()


class DashboardView(TemplateView):
    template_name = "dashboard.html"
    __doc__ = "This view is used to redirect the dashboard page"


class UserSignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"
    __doc__ = "This view is used to register a new user"


class UserLoginView(TemplateView):
    template_name = "login.html"
    __doc__ = "This view is used to login in our site"

    def post(self, request):
        username = request.POST.get("username")
        user = User.objects.filter(username=username).first()
        if user:
            username = user.username
            password = request.POST.get("password")
        else:
            messages.add_message(request, messages.INFO, "User doesn't exists ")
            return redirect("/login")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.add_message(
                request, messages.INFO, "Username or Password is incorrect."
            )
            return redirect("/login")


def logout(request):
    """
    This method is used to log out from current user
    """
    django_logout(request)
    return redirect("dashboard")
