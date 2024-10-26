from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    
    objects = UserManager()
    
    # فیلدی که باهاش کاربر رو اعتبار سنجی می کنیم
    USERNAME_FIELD = 'phone_number'
    
    # در زمان ایجاد کاربر چه فیلدهایی ضروری هستند
    REQUIRED_FIELDS = ['email', 'full_name']
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # پراپرتی در پایتون چیست؟
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    