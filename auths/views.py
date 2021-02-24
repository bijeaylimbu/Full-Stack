import os

import form as form
import jwt
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.shortcuts import  render, redirect
from django.conf import settings
from django.contrib.auth import login
from django.contrib import messages
from django_registration import views
from django.contrib.auth import get_user_model


User = get_user_model()
from drf_yasg import openapi
from rest_framework.authentication import TokenAuthentication
from django.urls import reverse

from rest_framework_simplejwt.tokens import RefreshToken
from verify_email.email_handler import send_verification_email
from django.contrib.auth import get_user_model
from .Utils import Util
from .token import account_activation_token

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, request, status, serializers
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.
from rest_framework import generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .serializers import UserSerializer, RegisterSerializer, EmailVerificationSerializer, ChangePasswordSerializer, \
    SetNewPasswordSerializer, ResetPasswordEmailRequestSerializer
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from verify_email.email_handler import send_verification_email
from drf_yasg.utils import swagger_auto_schema


class CustomRedirect(HttpResponsePermanentRedirect):

    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']

class UserAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterAPIView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     user = serializer.save()
    #
    #     return Response({
    #
    #         "user": UserSerializer(user, context=self.get_serializer_context()).data,
    #         # "token": AuthToken.objects.create(user)[1]
    #     })

    def post(self, request, *args, **kwargs):
        user = request.data

        serializer = self.serializer_class(data=user)
        # serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        user.is_active=False
        user.save()
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
        email_body = 'Hi ' + user.username + \
                     ' Use the link below to verify your email \n' + absurl
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email'}

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)

    # def register_user(request):
    #
    #
    #     if form.is_valid():
    #         inactive_user = send_verification_email(request, form)
    #         inactive_user.cleaned_data['email']





# class RegisterAPIView(generics.GenericAPIView):
#     queryset = User.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = RegisterSerializer
#
#
#     def post(self, request):
#         User.objects.get()
#         user = request.data
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         user_data = serializer.data
#         user = User.objects.get(email=user_data['email'])
#         token = RefreshToken.for_user(user).access_token
#         current_site = get_current_site(request).domain
#         relativeLink = reverse('email-verify')
#         absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
#         email_body = 'Hi ' + user.username + \
#                      ' Use the link below to verify your email \n' + absurl
#         data = {'email_body': email_body, 'to_email': user.email,
#                 'email_subject': 'Verify your email'}
#
#         Util.send_email(data)
#         return Response(user_data, status=status.HTTP_201_CREATED)









class VerifyEmail(generics.GenericAPIView):

    serializer_class = EmailVerificationSerializer

    permission_classes = (AllowAny,)
    # token_param_config = openapi.Parameter(
    #     'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    # @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY,algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()


            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError :
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)











#
# class SignupView(APIView):
#     permission_classes = (permissions.AllowAny, )
#
#     def post(self, request, format=None):
#         data = self.request.data

        # name = data['name']
        # email = data['email']
        # password = data['password']
        # password2 = data['password2']
        #
        # if password == password2:
        #     if User.objects.filter(email=email).exists():
        #         return Response({'error': 'Email already exists'})
        #     else:
        #         if len(password) < 6:
        #             return Response({'error': 'Password must be at least 6 characters'})
        #         else:
        #             user = User.objects.create_user(email=email, password=password, name=name)
        #
        #             user.save()
        #             return Response({'success': 'User created successfully'})
        # else:
        #     return Response({'error': 'Passwords do not match'})


#
# class ProfileAPIView(generics.GenericAPIView):
#         # queryset = Profile.objects.all()
#         # permission_classes = (AllowAny,)
#         # serializer_class = ProfileSerializer
#         queryset = Profile.objects.all()
#         serializer_class = ProfileSerializer
#         permission_classes = (
#             permissions.IsAuthenticatedOrReadOnly,
#         )
#
#         permission_classes = (IsAuthenticated,)
#         authentication_classes = (TokenAuthentication,)
#
#         permission_classes = [IsAuthenticated]
#         permission_classes = (AllowAny,)
#
#
#
#
#         def post(self, request):
#             serializer = ProfileSerializer(data=request.data)
#             for file_entry in request.FILES.getlist('files'):
#                 uploaded_file_name = file_entry.name
#                 uploaded_file_content = file_entry.read()
#                 uploaded_file_content.save()
#                 return uploaded_file_name
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 return Response(serializer.data)



class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data.get('email', '')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request=request).domain
            relativeLink = reverse(
                'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

            redirect_url = request.data.get('redirect_url', '')
            absurl = 'http://'+current_site + relativeLink
            email_body = 'Hello, \n Use link below to reset your password  \n' + \
                absurl+"?redirect_url="+redirect_url
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your passsword'}
            Util.send_email(data)
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    permission_classes = (AllowAny,)

    def get(self, request, uidb64, token):

        redirect_url = request.GET.get('redirect_url')

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return  Response({'error':"invalid token"})
            return  Response({'successs'})
            #     if len(redirect_url) > 3:
            #         return CustomRedirect(redirect_url + '?token_valid=False')
            #     else:
            #         return CustomRedirect(os.environ.get('FRONTEND_URL', '') + '?token_valid=False')
            #
            # if redirect_url and len(redirect_url) > 3:
            #     return CustomRedirect(
            #         redirect_url + '?token_valid=True&message=Credentials Valid&uidb64=' + uidb64 + '&token=' + token)
            # else:
            #     return CustomRedirect(os.environ.get('FRONTEND_URL', '') + '?token_valid=False')

        except DjangoUnicodeDecodeError as identifier:
            try:
                if not PasswordResetTokenGenerator().check_token(user):
                    return CustomRedirect(redirect_url + '?token_valid=False')

            except UnboundLocalError as e:
                return Response({'error': 'Token is not valid, please request a new one'},
                                status=status.HTTP_400_BAD_REQUEST)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    permission_classes = (AllowAny,)

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)


