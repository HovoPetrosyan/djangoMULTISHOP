from django.urls import path
from UserApp.views import user_logout, user_login

urlpatterns = [
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
]