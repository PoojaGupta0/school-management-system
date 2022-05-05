from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from core.schema import schema

from .views import (AllStudentListView, AllTeachersListView, DashboardView,
                    StudentAllTeachersListView, TeacherAllStudentListView,
                    UserLoginView, UserSignUpView, logout)

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("signup/", UserSignUpView.as_view(), name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", logout, name="logout"),
    path("all_teacher_list/", AllTeachersListView.as_view(), name="all_teachers_list"),
    path(
        "teacher_all_student_list/<int:teacher_id>/",
        TeacherAllStudentListView.as_view(),
        name="teacher_all_students_list",
    ),
    path(
        "graphql/",
        csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)),
        name="graphql_view",
    ),
    path("all_student_list/", AllStudentListView.as_view(), name="all_students_list"),
    path(
        "student_all_teacher_list/<int:student_id>/",
        StudentAllTeachersListView.as_view(),
        name="student_all_teacher_list",
    ),
]
