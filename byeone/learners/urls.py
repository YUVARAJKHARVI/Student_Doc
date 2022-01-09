from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Student_Info, name="Student_Info"),
    path("Add-Student/", views.Add_Student, name="Add_Student"),
    path("user/", views.Login, name="user"),
    path("Student_Academics_data/<Roll_no>", views.student_view, name="student_view"),
    path("Update/<Roll_no>", views.Update, name="update"),
    path("Delete/<Roll_no>", views.Delete, name="delete"),
    path("Link-Search/", views.Link_search, name="Link_search"),
    path("forgot_password/", views.forgot_password, name="forgot_password"),
    path("logout/", views.Logout, name="logout"),
]
