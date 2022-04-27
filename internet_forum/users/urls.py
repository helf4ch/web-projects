from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.LoginUser.as_view(), name="login"),
    path('signup/', views.RegisterUser.as_view(), name="signup"),
    path('<int:pk>/', views.UserProfile.as_view(), name="profile"),
    path('logout/', views.LogoutUser.as_view(), name="logout"),
]
