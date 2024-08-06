from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    class Type(models.TextChoices):
        USER = "user", 'user'
        ADMIN = 'admin', 'admin'

    created_at = models.DateTimeField(auto_now_add=True)
    birthday = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=255, choices=Type.choices, default=Type.USER)
    image = models.ImageField(upload_to='user/', blank=True, null=True)
    telegram_username = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username



class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models
# from general.choices import UserRoleChoice
# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('role', UserRoleChoice.premium_user.value)
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)

# class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to='user_image/', null=True, blank=True)
    role = models.CharField(max_length=15, choices=UserRoleChoice.choices, default=UserRoleChoice.user.value)
    objects = UserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def str(self):
        return self.email