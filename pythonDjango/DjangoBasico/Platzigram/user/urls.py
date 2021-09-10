"""Users URLs"""

# Django
from django.urls import path

# Views
from user import views

urlpatterns = [

    # Posts
    path(
        route = '<str:slug>', 
        view = views.UserDetailView.as_view(), 
        name='detail'
    ),

    # Management
    path(
        route = 'login/', 
        view = views.login_view, 
        name='login'
    ),
    path(
        route = 'logout/', 
        view = views.logout_view, 
        name='logout'
    ),
    path(
        route = 'signup/', 
        view = views.signup, 
        name='signup'
    ),
    path(
        route = 'me/profile/', 
        view = views.update_profile, 
        name='update'
    ),
]