from django.db import models
from User.models import user_m

# Create your models here.

class ticket_m(models.Model):
    id = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    priority = models.BooleanField(default= False)
    user_id = models.ForeignKey(user_m, on_delete = models.CASCADE)
    list_id = models.ManyToManyField('List.list_m')


class project_m(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)

class comment_m(models.Model):
     id = models.IntegerField(primary_key=True)
     content = models.ImageField(width_field=15, height_field=15)
     user_id = models.ForeignKey(user_m, on_delete = models.CASCADE)
     ticket_id = models.ForeignKey(ticket_m, on_delete = models.CASCADE)
     timestamp  = models.DateTimeField(auto_now_add=True)