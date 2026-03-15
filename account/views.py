from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
# Create your views here.
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
   

    serializer =RegisterSerializer(data=request.data)
    if serializer.is_valid():
        register=serializer.save()
        # register_mail.delay(
        #     register.email,
        #     register.last_name,
        #     register.first_name,
        #     register.role

        # )

        return Response({
            "data": serializer.data
        }, status =201)
    print(serializer.errors)
    return Response({
        "error":serializer.errors
    }, status=400)



@api_view(["GET"])
def get_users(request):
    users = User.objects.select_related("profile").all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)



@api_view(["GET", "PATCH"])
@permission_classes([IsAuthenticated])
def my_profile(request):

    if request.method == "GET":
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    if request.method == "PATCH":
        serializer = UserSerializer(
            request.user,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
        
    try:
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"error": "Refresh token is required"}, status=400)
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"detail": "Logout successful"})
    except Exception as e:
        print(str(e))
        return Response({"error": str(e)}, status=400)
       
