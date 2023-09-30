from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager

from django.db.models import Q

from .models import Post
from . serializers import PostSerializer, UserSerializer


class RegisterUser(APIView):
    def post(self, request):

        username = request.data.get('username')

        email = request.data.get('email')

        password = request.data.get('password')

        user_obj = User.objects.filter((Q(username=username) | Q(email=email))).first()

        if user_obj:
            return Response(
                {
                    'status': False,
                    'message': "You've already registered with this email or username",
                    'data': []
                },
                status=200
            )

        request_json = {
            'username': username,
            'email': email,
            'password': password,
        }

        user_serialized = UserSerializer(data=request_json)

        if user_serialized.is_valid():

            user_serialized.save()

            user_id = user_serialized.data.get('id')

            user_obj = User.objects.filter(id=user_id).first()

            if not user_obj:
                return False

            data = {
                'username': 'user_{0}'.format(int(user_id) * 71)
            }

            user_profile_serialized = UserSerializer(user_obj, data=data, partial=True)

            if not user_profile_serialized.is_valid():

                return Response(
                    {
                        'status': False,
                        'message': user_profile_serialized.errors,
                        'data': []
                    },
                    status=200
                )

            user_profile_serialized.save()

            return Response(
                {
                    'status': True,
                    'message': 'Registered successfully',
                    'data': []
                },
                status=200
            )

        else:
            return Response(
                {
                    'status': False,
                    'message': user_serialized.errors,
                    'data': []
                },
                status=200
            )


class Logout(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError,):
            pass

        return Response(
            {
                'status': True,
                'message': 'Logged out successfully',
                'data': []
            },
            status=200
        )


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

        post_serialized = PostSerializer(data=data)

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

        post = Post.objects.filter(id=post_id)

        post_obj = post.first()

        if not post_obj.author != request.user.id:
            return Response(
                {
                    'status': False,
                    'message': 'Access denied!',
                    'data': []
                },
                status=200
            )

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


class Delete(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, ]

    def get(self, request):

        post_id = request.GET.get('post_id')

        post_obj = Post.objects.filter(id=post_id)

        if not post_obj.author != request.user.id:
            return Response(
                {
                    'status': False,
                    'message': 'Access denied!',
                    'data': []
                },
                status=200
            )

        if not post_obj.first():
            return Response(
                {
                    'status': False,
                    'message': 'post object does not exist!',
                    'data': []
                },
                status=200
            )
        post_obj.delete()

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
