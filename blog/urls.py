from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . views import NewPost, PostList, ReturnPost, Edit, Delete


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('new-post', NewPost.as_view()),
    path('list', PostList.as_view()),
    path('edit', Edit.as_view()),
    path('delete', Delete.as_view()),
    path('return', ReturnPost.as_view())
]