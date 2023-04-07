from django.urls import path
from .views import SignupView
from .views import logout_view

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path('logout/', logout_view, name='logout'),
]
