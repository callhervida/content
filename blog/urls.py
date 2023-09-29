from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . views import NewPost, PostList


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('new-post', NewPost.as_view()),
    path('post-list', PostList.as_view())
]