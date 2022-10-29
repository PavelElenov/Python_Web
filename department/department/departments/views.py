from django import forms, http
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from department.departments.models import Employee
from department.departments.validators import validate_age


class DepartmentRegisterForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )


class CreateEmployee(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    age = forms.NumberInput(attrs={'class': 'form-control'})

    egn = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


def show_details(request):
    return render(request, 'index.html')


def home_page(request):
    return render(request, "home_page.html")


@csrf_exempt
def create_employee(request):
    if request.method == "GET":
        employee_form = CreateEmployee()
    else:
        first_name = request.POST['first name']
        last_name = request.POST['last name']
        print(first_name, last_name)
        return http.HttpResponse(f"{first_name} {last_name}")

    context = {
        'employee_form': employee_form,
    }
    return render(request, 'create_employee.html', context)


def create_department(request):
    if request.method == "GET":
        department_form = DepartmentRegisterForm()
    else:
        department_form = DepartmentRegisterForm(request.POST)
        if department_form.is_valid():
            return render(request, 'home_page.html')
    context = {
        'department_form': department_form,
    }
    return render(request, 'create_department.html', context)
