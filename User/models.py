from django.db import models
class user_m (models.Model):
    

    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    Email = models.CharField(max_length=255, null=True, blank=True)
    role= models.CharField(max_length=20)
    owner_id = models.BooleanField(default=False)
    picture = models.ImageField(width_field=12, height_field=12, null=True,blank=True)
    