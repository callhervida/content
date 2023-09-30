from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . views import RegisterUser, Logout, NewPost, PostList, ReturnPost, Edit, Delete


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('logout/', Logout.as_view()),
    path('register/', RegisterUser.as_view()),
    path('new-post/', NewPost.as_view()),
    path('list/', PostList.as_view()),
    path('edit/', Edit.as_view()),
    path('delete/', Delete.as_view()),
    path('return/', ReturnPost.as_view())
]