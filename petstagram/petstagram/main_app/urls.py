from django.urls import path

from petstagram.main_app.views import home_page, show_dashboard, show_profile_details, delete_user, create_profile

urlpatterns = (
    path('', home_page, name="home"),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('profile/', show_profile_details, name='profile'),
    path('delete/<int:pk>', delete_user, name='delete user'),
    path("create profile/", create_profile, name='create profile')
)
