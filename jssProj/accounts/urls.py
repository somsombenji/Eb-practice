from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]