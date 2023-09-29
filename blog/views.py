from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Post
from . serializers import PostSerializer


class NewPost(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, ]

    def post(self, request):

        author_id = request.user.id

        title = request.data.get('title')

        content = request.data.get('content')

        data = {
            'title': title,
            'content': content,
            'author': author_id
        }

        post_serialized = PostSerializer(data)

        if not post_serialized.is_valid():
            return Response(
                {
                    'status': False,
                    'message': post_serialized.errors,
                    'data': []
                },
                status=200
            )
        post_serialized.save()


class PostList(APIView):

    def post(self, request):

        post_obj = Post.objects.all()

        post_serialized = PostSerializer(post_obj, many=True)

        return Response(
            {
                'status': True,
                'message': 'success',
                'data': post_serialized.data
            },
            status=200
        )



