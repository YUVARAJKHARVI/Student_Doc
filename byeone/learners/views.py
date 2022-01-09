from django.shortcuts import render, redirect, HttpResponse
from .models import Students, Students_Academics
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
import requests
from bs4 import BeautifulSoup


# Create your views here.


def Student_Info(request):
    if request.method == "POST":

        name = request.POST["search_name"]
        Students_list = Students.objects.filter(Name=name)

        return render(request, "Student_Info.html", {"Students": Students_list})
    else:
        Students_list = Students.objects.all()
        Students_lit = Students_Academics.objects.all()

    return render(request, "Student_Info.html", {"Students": Students_list})


def Login(request):
    if request.method == "POST":

        if "login" in request.POST:

            username = request.POST["log_username"]
            password = request.POST["log_password"]
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect(Student_Info)

            else:
                messages.warning(request, "Please enter valid details.")
                return render(request, "sign_up.html")

        if "register" in request.POST:
            username = request.POST["username"]
            email = request.POST["email"]
            password1 = request.POST["password1"]
            password2 = request.POST["password2"]
            user = User.objects.create_user(username, email, password1)
            user.save()
            messages.success(request, "Account created successfully.")
            return redirect(Login)

    return render(request, "sign_up.html")


@login_required
def Logout(request):
    auth.logout(request)
    messages.warning(request, "Logout Successfully.")
    return redirect(Student_Info)


@login_required
def Add_Student(request):
    try:
        if request.method == "POST":
            name = request.POST["name"]
            roll_no = request.POST["roll_no"]
            clas = request.POST["class"]
            school = request.POST["school"]
            mobile = request.POST["mobile"]
            address = request.POST["address"]
            Maths = request.POST["Maths"]
            Physics = request.POST["Physics"]
            Chemistry = request.POST["Chemistry"]
            Biology = request.POST["Biology"]
            English = request.POST["English"]
            Student = Students.objects.create(
                Roll_no=roll_no,
                Name=name,
                Class=clas,
                School=school,
                Mobile=mobile,
                Address=address,
            )

            Students_Academic = Students_Academics.objects.create(
                Maths=Maths,
                Physics=Physics,
                Chemistry=Chemistry,
                Biology=Biology,
                English=English,
                Students=Student,
            )
            Student.save()
            Students_Academic.save()
            return redirect(Student_Info)
    except IntegrityError:
        messages.warning(request, "This student details already exist")
        return render(request, "Add_Student.html")
    return render(request, "Add_Student.html")


def student_view(request, Roll_no):
    Students_data = Students_Academics.objects.filter(Students=Roll_no)
    return render(request, "Student_details.html", {"Students_data": Students_data})


@login_required
def Update(request, Roll_no):
    if request.method == "POST":
        name = request.POST["name"]
        clas = request.POST["class"]
        school = request.POST["school"]
        mobile = request.POST["mobile"]
        address = request.POST["address"]
        Maths = request.POST["Maths"]
        Physics = request.POST["Physics"]
        Chemistry = request.POST["Chemistry"]
        Biology = request.POST["Biology"]
        English = request.POST["English"]

        Student_acdmcs = Students_Academics.objects.get(Students=Roll_no)
        Student = Students.objects.get(Roll_no=Roll_no)
        if name == "":
            name = Student.Name
        if clas == "":
            clas = Student.Class
        if school == "":
            school = Student.School
        if mobile == "":
            mobile = Student.Mobile
        if address == "":
            address = Student.Address

        if Maths == "":
            Maths = Student_acdmcs.Maths
        if Physics == "":
            Physics = Student_acdmcs.Physics
        if Chemistry == "":
            Chemistry = Student_acdmcs.Chemistry
        if Biology == "":
            Biology = Student_acdmcs.Biology
        if English == "":
            English = Student_acdmcs.English

        Student.Name = name
        Student.Class = clas
        Student.School = school
        Student.Mobile = mobile
        Student.Address = address
        Student.save()
        Student_acdmcs.Maths = Maths
        Student_acdmcs.Physics = Physics
        Student_acdmcs.Chemistry = Chemistry
        Student_acdmcs.Biology = Biology
        Student_acdmcs.English = English
        Student_acdmcs.save()
        return redirect(Student_Info)
    Students_data = Students_Academics.objects.filter(Students=Roll_no)
    return render(request, "update.html", {"Students_data": Students_data})


@login_required
def Delete(request, Roll_no):
    Student = Students.objects.get(Roll_no=Roll_no)
    Student.delete()
    return redirect(Student_Info)


def forgot_password(request):
    if request.method == "POST":

        if "Email_verification" in request.POST:
            email = request.POST["reset_email"]
            username = request.POST["username"]
            try:
                user = User.objects.get(username=username, email=email)
                request.session["email"] = email
                return render(request, "forgot_password.html", {"email": email})

            except User.DoesNotExist:
                messages.warning(
                    request, "Email addres not exist. Please register first."
                )

        if "Reset_password" in request.POST:
            password = request.POST["reset_password"]
            email = request.session["email"]

            u = User.objects.get(email=email)
            u.set_password(password)
            u.save()
            return redirect(Login)
    return render(request, "forgot_password.html")


def Link_search(request):
    if request.method == "POST":
        link = request.POST["link"]
        url = link
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, "html.parser")
        urls = []
        for link in soup.find_all("a"):
            print(link.get("href"))
            urls.append(link.get("href"))
        return render(request, "Link_search.html", {"urls": urls})
    return render(request, "Link_search.html")
