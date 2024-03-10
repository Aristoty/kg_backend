from django.urls import path
from .views import register, login, user_view, logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('user/', user_view, name='user'),
    path('logout/', logout, name='logout'),
]
