from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extera_fields):
        """
        Create and return a regular user with a phone number and password.
        """

        if not email:
            raise ValueError("The email must be set")
        user = self.model(email=email, **extera_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None, **extera_fields):
        extera_fields.setdefault('is_staff', True)
        extera_fields.setdefault('is_admin', True)

        return self.create_user(email, password, **extera_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email', unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    
