from django.urls import path
from users.views import UserListView, UserLoginView, UserLogoutView, UserSignUpView 


app_name = 'users'

urlpatterns = [
    path('list',UserListView.as_view(),name='list_users'), 
    path('login', UserLoginView.as_view(),name='login_users'),   
    path('logout', UserLogoutView.as_view(),name='logout_users'),
    path('signup', UserSignUpView.as_view(),name='signup_users'),
]