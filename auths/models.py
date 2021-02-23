# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
#
#
# class UserAccountManager(BaseUserManager):
#     def create_user(self, email, name, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         email = self.normalize_email(email)
#         user = self.model(email=email, name=name)
#
#         user.set_password(password)
#         user.save()
#
#         return user
#
#     def create_superuser(self, email, name, password):
#         user = self.create_user(email, name, password)
#
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#
#         return user
#
#
# class UserAccount(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     objects = UserAccountManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']
#
#     def get_full_name(self):
#         return self.name
#
#     def get_short_name(self):
#         return self.name
#
#     def __str__(self):
#         return self.email


from django.contrib.auth.models import User, UserManager
from django.contrib.auth.password_validation import validate_password
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
#
# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True, null=True)
#
#     is_staff = models.BooleanField(
#         _('staff status'),
#         default=False,
#         help_text=_('Designates whether the user can log into this site.'),
#     )
#     is_active = models.BooleanField(
#         _('active'),
#         default=True,
#         help_text=_(
#             'Designates whether this user should be treated as active. '
#             'Unselect this instead of deleting accounts.'
#         ),
#     )
#
#
#     def __str__(self):
#         return self.email
#
#     def get_full_name(self):
#         return self.email
#
#     def get_short_name(self):
#         return self.email
#
#
#
#
# class CustomUser(AbstractUser):
#     username = None
#     phone_number = models.IntegerField(null=True)
#     address = models.CharField(max_length=10)
#     email = models.EmailField(_('email address'), unique=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#
#
#     spouse_name = models.CharField(blank=True, max_length=100)
#     date_of_birth = models.DateField(blank=True, null=True)
#
#     def __str__(self):
#         return self.email
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


# class CustomUser(AbstractUser):
#
#     email = models.EmailField(_('email address'), unique=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = CustomUserManager()
#
#     def __str__(self):
#         return self.email


# class Profile(models.Model):
#
#     phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='phone')
#     password = models.CharField(max_length=255,default='')
#     # password2 = models.CharField(max_length=255,default='')
#
#     email = models.EmailField(max_length=255,default='')
#
#
#     first_name=models.CharField(max_length=255,default='')
#
#     last_name = models.CharField(max_length=255,default='')
#     username = models.CharField(max_length=255,default='')




AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}



# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=255, unique=True, db_index=True)
#     email = models.EmailField(max_length=255, unique=True, db_index=True)
#     is_verified = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     auth_provider = models.CharField(
#         max_length=255, blank=False,
#         null=False, default=AUTH_PROVIDERS.get('email'))
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#
#     objects = UserManager()
#
#     def __str__(self):
#         return self.email
#
#     def tokens(self):
#         refresh = RefreshToken.for_user(self)
#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token)
#         }



class UserProfile(models.Model):
    # username = models.CharField(blank=True, max_length=255,unique=True)
    # password = models.CharField(blank=True,max_length=255,default='')
    # user_id = models.OneToOneField(User, on_delete=models.CASCADE,default='')
    phone = models.CharField(blank=False,max_length=255,)
    password2 = models.CharField(blank=False, max_length=255,default="")
    is_verified = models.BooleanField(default=False)



@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )