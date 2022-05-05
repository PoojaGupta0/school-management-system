from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, TemplateView

from core.models import Student, Teacher, TeachersOfStudent

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


class AllTeachersListView(ListView):
    model = Teacher
    context_object_name = "all_teachers_list"
    template_name = "all_teachers_list.html"
    __doc__ = "This view is used to the the list of all teachers"


class TeacherAllStudentListView(ListView):
    model = TeachersOfStudent
    template_name = "teacher_all_students_list.html"
    __doc__ = "This view is used to get the list of all student of associated teacher"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teacher_all_students_list"] = TeachersOfStudent.objects.filter(
            teacher_id=self.kwargs.get("teacher_id")
        )
        context["teacher"] = Teacher.objects.filter(
            id=self.kwargs.get("teacher_id")
        ).first()
        return context


class AllStudentListView(ListView):
    model = Student
    context_object_name = "students_list"
    template_name = "all_students_list.html"
    __doc__ = "This view is used to get the list of all Students"


class StudentAllTeachersListView(ListView):
    model = TeachersOfStudent
    template_name = "student_all_teachers_list.html"
    __doc__ = "This view is used to get the list of all teachers of associated student"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["student_all_teacher_list"] = TeachersOfStudent.objects.filter(
            student=self.kwargs.get("student_id")
        )
        context["student"] = Student.objects.filter(
            id=self.kwargs.get("student_id")
        ).first()
        return context
