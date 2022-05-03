from django.urls import path

from .views import DashboardView, UserLoginView, UserSignUpView, logout

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("signup/", UserSignUpView.as_view(), name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", logout, name="logout"),
]
