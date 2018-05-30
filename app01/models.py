from django.db import models

# Create your models here.
class Role(models.Model):
    title=models.CharField(max_length=32)

    def __str__(self):
        return self.title

class UserGroup(models.Model):
    title=models.CharField(max_length=32)
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    user=models.CharField(max_length=32)
    email=models.EmailField()
    ug=models.ForeignKey(UserGroup,null=True,blank=True)
    m2m=models.ManyToManyField("Role")
    def __str__(self):
        return self.user

