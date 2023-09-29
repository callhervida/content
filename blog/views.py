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

        if not post_obj:
            return Response(
                {
                    'status': False,
                    'message': 'post object does not exist!',
                    'data': []
                },
                status=200
            )

        post_serialized = PostSerializer(post_obj, many=True)

        return Response(
            {
                'status': True,
                'message': 'success',
                'data': post_serialized.data
            },
            status=200
        )


class Edit(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, ]

    def post(self, request):

        post_id = request.data.get('post_id')

        title = request.data.get('title')

        content = request.data.get('content')

        post_obj = Post.objects.filter(id=post_id)

        if not post_obj.first():
            return Response(
                {
                    'status': False,
                    'message': 'post object does not exist!',
                    'data': []
                },
                status=200
            )
        if title:
            post_obj.update(title=title)

        if content:
            post_obj.update(content=content)

        return Response(
            {
                'status': True,
                'message': 'success',
                'data': []
            },
            status=200
        )


class ReturnPost(APIView):

    def get(self, request):

        post_id = request.GET.get('post_id')


        if not post_id:
            return Response(
                {
                    'status': False,
                    'message': 'Insert title or id',
                    'data': []
                },
                status=200
            )

        post_obj = Post.object.filter(id=post_id).first()

        if not post_obj:
            return Response(
                {
                    'status': False,
                    'message': 'post object does not exist!',
                    'data': []
                },
                status=200
            )
        
        title = post_obj.title

        content = post_obj.content

        author = post_obj.author

        created_at = post_obj.created_at

        return Response(
            {
                'status': False,
                'message': 'Insert title or id',
                'data': [
                    {
                        'title': title,
                        'content': content,
                        'author': author,
                        'created_at': created_at
                    }
                ]
            },
            status=200
        )
