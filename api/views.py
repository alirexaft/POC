from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import User
from api.serializers import LoginWithPasswordSerializer


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
            print(serializer.validated_data)
            password = serializer.validated_data['password']
            print(User.objects.filter(username=username))
            if not User.objects.filter(username=username).exists():
                return Response(data={
                    "message": "user not found",
                    "success": False,
                    "status": 404
                }, status=status.HTTP_404_NOT_FOUND)

            user = User.objects.get(username=username)

            if check_password(password, user.password):
                token = get_tokens_for_user(user)
                return Response(data={
                    "message": "success",
                    "status": 200,
                    "success": True,
                    "data": {
                        "tokens": {
                            "refreshToken": token["refresh"],
                            "accessToken": token["access"]
                        }
                    }
                })

            else:
                return Response(data={
                    "message": "username or password is wrong!",
                    "status": 404,
                    "success": False,

                }, status=404)

        else:
            return Response(data={
                "message": "data is not valid!",
                "status": 422,
                "success": False,
                "errors": serializer.errors
            }, status=422)

        #         if check_password(password, user.password) and ((user.password is not None) or (user.password != "")):
        #             token = get_tokens_for_user(user)
        #             return Response(data={
        #                 "message": "با موفقیت وارد شدید",
        #                 "status": 200,
        #                 "success": True,
        #                 "data": {
        #                     "tokens": {
        #                         "refreshToken": token["refresh"],
        #                         "accessToken": token["access"]
        #                     },
        #                     "user": {
        #                         "id": user.pk,
        #                         "role": user.role.id if user.role else "",
        #                         "status": user.status,
        #                         "fullName": user.fullName if user.fullName else "",
        #                         "profile": user.profile if user.profile else "",
        #                         "state": {"name": user.state if user.state == None else user.state.name,
        #                                   "id": user.state if user.state == None else user.state.id},
        #                         "city": {"name": user.city if user.city == None else user.city.name,
        #                                  "id": user.city if user.city == None else user.city.id},
        #                         "address": user.address if user.address else "",
        #                         "postalCode": user.postalCode if user.postalCode else "",
        #                         "shebaCode": user.shebaCode if user.shebaCode else "",
        #                     }
        #                 }
        #             }, status=status.HTTP_200_OK)
        #
        #         else:
        #             return Response(data={'message': 'کاربر یافت نشد', 'status': 404, "success": False},
        #                             status=status.HTTP_404_NOT_FOUND)
        #
        #     except:
        #         return Response(data={'message': 'کاربر یافت نشد', 'status': 404, "success": False},
        #                         status=status.HTTP_404_NOT_FOUND)
        #
        # else:
        #     return Response(data={'message': 'اطلاعات وارد شده معتبر نیست', 'status': 422, "success": False},
        #                     status=status.HTTP_422_UNPROCESSABLE_ENTITY)
