from django.contrib.auth.hashers import check_password
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import User
from api.serializers import LoginWithPasswordSerializer, RegisterSerializer
from djangoProjectPOC.myFunction import myFunction
from .models import MetaData
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class LoginWithPassword(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = LoginWithPasswordSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            if not User.objects.filter(username=username).exists():
                return Response(data={
                    "message": "user not found",
                    "success": False,
                    "status": 404
                }, status=status.HTTP_404_NOT_FOUND)

            user = User.objects.get(username=username)

            if check_password(password, user.password):
                token = get_tokens_for_user(user)
                user.last_login = timezone.now()

                return Response(data={
                    "message": "success",
                    "status": 200,
                    "success": True,
                    "data": {
                        "tokens": {
                            "refreshToken": token["refresh"],
                            "accessToken": token["access"]
                        },
                        "user": {
                            "id": user.pk,
                            "username": user.username
                        }
                    }
                })

            else:
                return Response(data={
                    "message": "username or password is wrong!",
                    "status": 403,
                    "success": False,

                }, status=403)

        else:
            return Response(data={
                "message": "data is not valid!",
                "status": 422,
                "success": False,
                "errors": serializer.errors
            }, status=422)


class TestAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(data={
            "message": "Yes"
        }, status=200)


class RegisterAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            if User.objects.filter(username=username).exists():
                return Response(data={
                    "message": "User exists",
                    "success": False,
                    "status": 409
                }, status=status.HTTP_409_CONFLICT)

            user = User(username=username)
            user.set_password(password)

            if "first_name" in serializer.validated_data.keys():
                user.first_name = serializer.validated_data['first_name']

            if "last_name" in serializer.validated_data.keys():
                user.last_name = serializer.validated_data['last_name']
            user.save()
            token = get_tokens_for_user(user)

            return Response(data={
                "message": "user created successfully",
                "status": 201,
                "success": True,
                "data": {
                    "tokens": {
                        "refreshToken": token["refresh"],
                        "accessToken": token["access"]
                    },
                    "user": {
                        "id": user.pk,
                        "username": user.username
                    }
                }
            }, status=201)
        else:
            return Response(data={
                "message": "data is not valid!",
                "status": 422,
                "success": False,
                "errors": serializer.errors
            }, status=422)


class MainRequestAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
            metdata = MetaData()
            metdata.request_date = timezone.now()
            metdata.request_user = self.request.user
            line_count = myFunction()

            metdata.line_count = line_count
            metdata.end_req_time = timezone.now()
            metdata.save()

            return Response(data={
                "message": "data saved successfully",
                "status": 201,
                "success": True,
                "data": {
                    "id": metdata.pk,
                    "requestTime": metdata.request_date,
                    "end_req_time": metdata.end_req_time,
                    "lineCount": metdata.line_count
                }
            })
