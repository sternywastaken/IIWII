from django.urls import path
from .views import home, register, user_login, user_logout, dashboard, create_post, post_comment, view_post, delete_post

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='user-register'),
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout'),
    path('dashboard/', dashboard, name='user-dashboard'),
    path('create_post/', create_post, name='user-post'),
    path('post_comment/<int:id>', post_comment, name='post-comment'),
    path('view_post/<int:id>/', view_post, name='view-post'),
    path('delete_post/<int:id>/', delete_post, name='delete-post'),
]
