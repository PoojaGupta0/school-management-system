from django.urls import path

from .views import (AllTeachersListView, DashboardView,
                    TeacherAllStudentListView, UserLoginView, UserSignUpView,
                    logout)

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("signup/", UserSignUpView.as_view(), name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", logout, name="logout"),
    path("logout/", logout, name="logout"),
    path("all_teacher_list/", AllTeachersListView.as_view(), name="all_teachers_list"),
    path(
        "teacher_all_student_list/<int:teacher_id>/",
        TeacherAllStudentListView.as_view(),
        name="teacher_all_students_list",
    ),
]
