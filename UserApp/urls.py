from django.urls import path
from UserApp.views import (user_logout,
                           user_login,
                           user_register,
                           user_profile,
                           user_update,
                           user_password,
                           user_comments,
                           comment_delete)

urlpatterns = [
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('profile/', user_profile, name='userprofile'),
    path('user_update/', user_update, name='user_update'),
    path('password_update/', user_password, name='user_password'),
    path('user_comment/', user_comments, name='user_comments'),
    path('user_comment_delete/<int:id>/', comment_delete, name='comment_delete'),
]
