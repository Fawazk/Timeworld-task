from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db.models.deletion import CASCADE

# Create your models here.


Role=(
    ('student','student'),
    ('staff','staff'),
    ('editor','editor'),
)
class MyAccountManager(BaseUserManager):
    def create_user(self,Name,Mobile,email,Role,Nationality,Country,password=None):
        if not email:
            raise ValueError('User must have an email address ')

        if not Name:
            raise ValueError('User must have an Name')
        if not Role:
            raise ValueError('User must have an Role')
        if not Nationality:
            raise ValueError('User must have an Nationality')
        if not Country:
            raise ValueError('User must have an country')
        user = self.model(
            email = self.normalize_email(email),
            Name = Name,
            Mobile = Mobile,
            Nationality=Nationality,
            Country=Country,
        )
        user.is_active=True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,Name,email,password,Mobile):
        user = self.create_user(
            email=self.normalize_email(email),
            Name=Name,
            password=password,
            Mobile=Mobile,

        )
        user.is_admin = True
        user.is_active =True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    Name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,unique=True)
    Mobile = models.CharField(('Mobile'), max_length=10,unique=True)
    Role = models.CharField(max_length=200,choices=Role,default='student')
    Country = models.CharField(max_length=50,null=True)
    Nationality = models.CharField(max_length=50,null=True)
    is_admin = models.BooleanField(default=False)

    # required
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['Name','Mobile','Role','Country','Nationality']

    objects = MyAccountManager()

    def _str_(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_labels): 
        return True