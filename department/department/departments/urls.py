from django.urls import path

from department.departments.views import show_details, home_page, create_employee, create_department

urlpatterns = (
    path('', home_page, name='home'),
    path('department/', show_details, name='department'),
    path('create employee/', create_employee, name='create employee'),
    path('create department/', create_department, name='create department'),
)